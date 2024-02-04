from manim import *

class MySquare(Square):
    @override_animation(FadeIn)
    def _fade_in_animation(self, **kwargs):
        return Create(self, **kwargs)
  
class MySqaureExample(Scene):
  def construct(self):
    self.play(FadeIn(MySquare()))
  
      
class AnimationBoundary(Scene):
    def construct(self):
        text = Text("Hello, world")
        boundary = AnimatedBoundary(text, colors = [RED, GREEN, BLUE], cycle_rate = 3)
        self.add(text, boundary)
        self.wait(2)
        
class AnimatedBoundaryExample(Scene):
    def construct(self):
        text = Text("So shiny!")
        boundary = AnimatedBoundary(text, colors=[RED, GREEN, BLUE],
                                    cycle_rate=3)
        self.add(text, boundary)
        self.wait(2)
        
class TracedPathExample(Scene):
    def construct(self):
        circ = Circle(color=RED)
        circ.move_to(LEFT*4)
        dot = Dot(color=RED).move_to(circ.get_start())
        rolling_circle = VGroup(circ, dot)
        trace = TracedPath(circ.get_start)
        rolling_circle.add_updater(lambda m: m.rotate(-0.3))
        self.add(trace,rolling_circle)
        self.play(rolling_circle.animate.shift(RIGHT*8), run_time=4, rate_func=linear)
class TracedExample1(Scene):
    	def construct(self):
            circ = Circle(color=RED).shift(LEFT*4)
            dot = Dot(color=RED).move_to(circ.get_start())
            rolling_circle = VGroup(circ, dot)
            trace = TracedPath(circ.get_start)
            rolling_circle.add_updater(lambda m: m.rotate(-0.3))
            self.add(trace, rolling_circle)
            self.play(rolling_circle.animate.shift(RIGHT*8), run_time=4, rate_func=linear)
