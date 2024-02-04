## Manim 学习

https://docs.manim.community/en/stable/reference/manim.animation.changing.TracedPath.html

### Animations

#### Animation

1. 可以重写一个动画，比如，将FadeIn， 动画重写为create 创建

   ```python
   class MySquare(Square):
     @override_animation(FadeIn)
     def _fade_in_animation(self, **kwargs):
       return Create(self, **kwargs)
     
   class MySqaureExample(Scene):
     def construct(self):
       self.play(FadeIn(MySquare()))
   ```

#### Changing

1. AnimatedBoundary 可以让字体的边界（或者是物体的边界）？

   ```python
   class AnimationBoundary(Scene):
   	def construct(self):
       text = Text("Hello, world")
       boundary = AnimatedBoundary(text, colors = [RED, BLUE, GREEN], cycle_rate = 3)
       self.add(text, boundary)
       self.wait(2)
   ```

2. TracedPath 可以跟踪一个点的动画等等。

   ```python
   class TracedExample(Scene):
   	def construct(self):
       circ = Circle(color=RED).shift(Left*4)
       dot = Dot(color=RED).move_to(circ.get_start())
       rolling_circle = VGroup(circ, dot)
       trace = TracedPath(circ.get_start)
       rolling_circle.add_updator(lambda m: m.rotate(-0.3))
       self.add(trace rolling_circle)
       self.play(rolling_circle.animate.shift(RIGHT*8), run_time=4, rate_func=linear)
   ```

   