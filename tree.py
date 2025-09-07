from manim import *

# 自定义树节点外观（圆形 + 文字）
class TreeNodeVM(VGroup):
    def __init__(self, value, radius=0.4, color=BLUE, **kwargs):
        super().__init__(**kwargs)
        self.circle = Circle(radius=radius, color=color, stroke_width=3)
        self.label = Text(str(value), font_size=24).move_to(self.circle.get_center())
        self.add(self.circle, self.label)
        self.value = value

    def get_center(self):
        return self.circle.get_center()

    def get_left(self):
        return self.circle.get_left()

    def get_right(self):
        return self.circle.get_right()

class BuildTreeAnimation(Scene):
    def construct(self):
        # ========== 第1部分：展示输入数组 ==========
        title = Text("根据中序和后序遍历构造二叉树", font_size=36).to_edge(UP)
        self.play(Write(title))

        inorder = [9, 3, 15, 20, 7]
        postorder = [9, 15, 7, 20, 3]

        # 创建数组显示对象
        inorder_text = Text("中序: ", font_size=28, color=YELLOW)
        postorder_text = Text("后序: ", font_size=28, color=YELLOW)

        inorder_arr = self.create_array(inorder, GREEN)
        postorder_arr = self.create_array(postorder, BLUE)

        inorder_group = VGroup(inorder_text, inorder_arr).arrange(RIGHT).next_to(title, DOWN, buff=0.8)
        postorder_group = VGroup(postorder_text, postorder_arr).arrange(RIGHT).next_to(inorder_group, DOWN, buff=0.5)

        self.play(Write(inorder_group), Write(postorder_group))
        self.wait(1)

        # ========== 第2部分：初始化递归栈说明 ==========
        stack_title = Text("递归调用栈:", font_size=24).to_edge(LEFT).shift(UP * 2.5)
        self.play(Write(stack_title))
        stack_entries = VGroup().next_to(stack_title, DOWN, aligned_edge=LEFT)

        # ========== 第3部分：开始递归构建 ==========
        # 用于存储已创建的节点，避免重复创建
        node_map = {}

        # 存储中序索引映射（模拟代码中的哈希表）
        inorder_map = {val: idx for idx, val in enumerate(inorder)}

        # 树根位置
        root_pos = DOWN * 0.5

        # 开始递归动画
        tree_root = self.build_tree_animated(
            inorder, postorder, 
            0, len(inorder)-1, 
            0, len(postorder)-1,
            inorder_map,
            inorder_arr, postorder_arr,
            stack_entries, node_map,
            root_pos
        )

        self.wait(2)

        # ========== 第4部分：最终展示完整树 ==========
        final_title = Text("✅ 最终构造的二叉树", font_size=30, color=GREEN).to_edge(UP)
        self.play(
            FadeOut(title), FadeOut(inorder_group), FadeOut(postorder_group),
            FadeOut(stack_title), FadeOut(stack_entries),
            ReplacementTransform(title.copy(), final_title)
        )

        # 居中显示树
        self.play(tree_root.animate.move_to(ORIGIN).scale(1.2))
        self.wait(3)

    def create_array(self, arr, color):
        """创建带方框和数字的数组可视化"""
        squares = VGroup()
        texts = VGroup()
        for i, val in enumerate(arr):
            square = Square(side_length=0.7, color=color, stroke_width=2)
            text = Text(str(val), font_size=24).move_to(square.get_center())
            square_with_text = VGroup(square, text)
            squares.add(square)
            texts.add(text)
        squares.arrange(RIGHT, buff=0.1)
        return VGroup(squares, texts)

    def highlight_range(self, array_group, start, end, color=YELLOW):
        """高亮数组中某个范围"""
        squares = array_group[0]  # 方框组
        animations = []
        for i in range(len(squares)):
            if start <= i <= end:
                animations.append(squares[i].animate.set_fill(color, opacity=0.3))
            else:
                animations.append(squares[i].animate.set_fill(WHITE, opacity=0))
        return animations

    def build_tree_animated(self, inorder, postorder, in_start, in_end, post_start, post_end,
                           inorder_map, inorder_vg, postorder_vg, stack_entries, node_map, pos):
        """递归构建树并生成动画"""

        # 终止条件
        if post_start > post_end:
            return None

        # 获取当前根值
        root_val = postorder[post_end]

        # 创建栈条目
        stack_entry = Text(f"build({in_start},{in_end}, {post_start},{post_end})", font_size=18, color=WHITE)
        stack_entries.add(stack_entry)
        stack_entries.arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        stack_entries[-1].to_edge(LEFT).shift(DOWN * 0.5)

        self.play(Write(stack_entry))

        # 高亮当前范围
        self.play(
            *self.highlight_range(inorder_vg, in_start, in_end, GREEN),
            *self.highlight_range(postorder_vg, post_start, post_end, BLUE),
            run_time=0.8
        )

        # 创建节点（如果未创建过）
        if root_val not in node_map:
            node = TreeNodeVM(root_val, color=TEAL if root_val == postorder[-1] else BLUE)
            node.move_to(pos)
            node_map[root_val] = node
            self.play(Create(node.circle), Write(node.label), run_time=0.6)
        else:
            node = node_map[root_val]

        # 在后序数组中闪烁根节点
        root_square = postorder_vg[0][post_end]
        self.play(Indicate(root_square, color=RED, scale_factor=1.3), run_time=0.8)

        # 找到根在中序中的位置
        root_idx = inorder_map[root_val]
        left_size = root_idx - in_start

        # 计算子节点位置
        left_pos = pos + LEFT * 2 + UP * 1.2
        right_pos = pos + RIGHT * 2 + UP * 1.2

        # 构建左子树
        if left_size > 0:
            left_child = self.build_tree_animated(
                inorder, postorder,
                in_start, root_idx - 1,
                post_start, post_start + left_size - 1,
                inorder_map, inorder_vg, postorder_vg,
                stack_entries, node_map, left_pos
            )
            if left_child:
                # 创建连接线
                edge = Line(node.get_left(), left_child.get_right(), color=GRAY)
                self.play(Create(edge), run_time=0.5)
                node.add(edge)  # 可选：绑定到父节点

        # 构建右子树
        if in_end > root_idx:
            right_child = self.build_tree_animated(
                inorder, postorder,
                root_idx + 1, in_end,
                post_start + left_size, post_end - 1,
                inorder_map, inorder_vg, postorder_vg,
                stack_entries, node_map, right_pos
            )
            if right_child:
                edge = Line(node.get_right(), right_child.get_left(), color=GRAY)
                self.play(Create(edge), run_time=0.5)
                node.add(edge)

        # 从栈中移除当前条目（模拟返回）
        self.play(FadeOut(stack_entry), run_time=0.3)
        stack_entries.remove(stack_entry)

        return node