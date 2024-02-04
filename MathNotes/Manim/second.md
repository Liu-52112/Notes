```python
from manim import *
```


<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">Manim Community <span style="color: #008000; text-decoration-color: #008000">v0.17.3</span>

</pre>




```python
%%manim -qm -v WARNING SquareToCircle
class SquareToCircle(Scene):
   def construct(self):
      square = Square()
      circle = Circle()
      circle.set_fill(PINK, opacity=0.5)
      self.play(Create(square))
      self.play(Transform(square, circle))
      self.wait()
```

                                                                                    


<video src="media/jupyter/SquareToCircle@2024-02-04@20-58-46.mp4" controls autoplay loop style="max-width: 60%;"  >
      Your browser does not support the <code>video</code> element.
    </video>

