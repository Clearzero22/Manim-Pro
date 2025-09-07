from manim import *

class BuildTreeAnimation(Scene):
    def construct(self):
        # 展示初始数组
        inorder = Text("inorder: [9, 3, 15, 20, 7]").to_edge(UP)
        postorder = Text("postorder: [9, 15, 7, 20, 3]").next_to(inorder, DOWN)
        self.play(Write(inorder), Write(postorder))

        # 创建根节点 3
        root = Circle(radius=0.5, color=BLUE).shift(DOWN)
        root_label = Text("3").move_to(root.get_center())
        self.play(Create(root), Write(root_label))

        # 创建左子 9
        left = Circle(radius=0.4, color=GREEN).next_to(root, LEFT*2 + UP)
        left_label = Text("9").move_to(left.get_center())
        left_edge = Line(root.get_left(), left.get_right())
        self.play(Create(left), Write(left_label), Create(left_edge))

        # 创建右子 20
        right = Circle(radius=0.5, color=GREEN).next_to(root, RIGHT*2 + UP)
        right_label = Text("20").move_to(right.get_center())
        right_edge = Line(root.get_right(), right.get_left())
        self.play(Create(right), Write(right_label), Create(right_edge))

        # 创建 20 的左子 15
        right_left = Circle(radius=0.4, color=RED).next_to(right, LEFT + UP)
        rl_label = Text("15").move_to(right_left.get_center())
        rl_edge = Line(right.get_left(), right_left.get_right())
        self.play(Create(right_left), Write(rl_label), Create(rl_edge))

        # 创建 20 的右子 7
        right_right = Circle(radius=0.4, color=RED).next_to(right, RIGHT + UP)
        rr_label = Text("7").move_to(right_right.get_center())
        rr_edge = Line(right.get_right(), right_right.get_left())
        self.play(Create(right_right), Write(rr_label), Create(rr_edge))

        self.wait(3)