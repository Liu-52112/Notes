# Knot-insert

https://pages.mtu.edu/~shene/COURSES/cs3621/NOTES/spline/NURBS-knot-insert.html

The meaning of knot insertion is adding a new knot into the exiting knot vector without __changing the shape of the curve__.

## Why knot insertion



We know that the components of a nurbs curve is that the knots vector, control points and the degree, also the weights. And the degree of the curve can't be changed, so we must change the control points and the  knots vector. 

Because of the fundamental equlity $m = n +p +1$, after adding a new knot, the value of $m$ is increased by one and consequently, either the number of control points or the degree of the curve must also be increased by one.  Changing the degree of the curve will change the shape of the curve globally and will not be considered. Therefore, inserting a new knot causes a new control point to be added. In fact, some existing control points are removed and replaced with new ones by __corner cutting__.



