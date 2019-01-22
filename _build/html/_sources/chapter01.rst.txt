Chapter
=======

Section
-------

Subsection
~~~~~~~~~~

Text

Extensions
----------

MathJax
~~~~~~~

In text: :math:`\lim_{x\to a^-} f(x) = \pm \infty`, or

.. math::
    \overline{x}=\frac{M_{x=0}}{m} = \frac{\sum_{i=1}^n x_im_i}{\sum_{i=1}^n m_i}\mbox{asdfasdf}.


Sage-cell extensions 
--------------------

For the pdf-version the applets can be changed for static images.

R
~~~~

.. sagecell::
    :lang: R

    4+4
    
Sage
~~~~

Sage example by `Marshall Hampton <http://wiki.sagemath.org/interact/graphics#Curves_of_Pursuit>`_.

.. sagecell::

    npi = RDF(pi)
    def rot(t):
        from math import cos, sin
        return matrix([[cos(t),sin(t)],[-sin(t),cos(t)]])

    def pursuit(n,x0,y0,lamb,steps = 100, threshold = .01):
        paths = [[[x0,y0]]]
        for i in range(1,n):
            rx,ry = list(rot(2*npi*i/n)*vector([x0,y0]))
            paths.append([[rx,ry]])
        oldpath = [x[-1] for x in paths]
        for q in range(steps):
            diffs = [[oldpath[(j+1)%n][0]-oldpath[j][0],oldpath[(j+1)%n][1]-oldpath[j][1]] for j in range(n)]
            npath = [[oldpath[j][0]+lamb*diffs[j][0],oldpath[j][1]+lamb*diffs[j][1]] for j in range(n)]
            for j in range(n):
                paths[j].append(npath[j])
            oldpath = npath
        return paths
    html('<h3>Curves of Pursuit</h3>')
    @interact
    def curves_of_pursuit(n = slider([2..20],default = 5, label="# of points"),steps = slider([floor(1.4^i) for i in range(2,18)],default = 10, label="# of steps"), stepsize = slider(srange(.01,1,.01),default = .2, label="stepsize"), colorize = selector(['BW','Line color', 'Filled'],default = 'BW')):
        outpaths = pursuit(n,0,1,stepsize, steps = steps)
        mcolor = (0,0,0)
        outer = line([q[0] for q in outpaths]+[outpaths[0][0]], rgbcolor = mcolor)
        polys = Graphics()
        if colorize=='Line color':
            colors = [hue(j/steps,1,1) for j in range(len(outpaths[0]))]
        elif colorize == 'BW':
            colors = [(0,0,0) for j in range(len(outpaths[0]))]
        else:
            colors = [hue(j/steps,1,1) for j in range(len(outpaths[0]))]
            polys = sum([polygon([outpaths[(i+1)%n][j+1],outpaths[(i+1)%n][j], outpaths[i][j+1]], rgbcolor = colors[j]) for i in range(n) for j in range(len(outpaths[0])-1)])
            #polys = polys[0]
            colors = [(0,0,0) for j in range(len(outpaths[0]))]
        nested = sum([line([q[j] for q in outpaths]+[outpaths[0][j]], rgbcolor = colors[j]) for j in range(len(outpaths[0]))])
        lpaths = [line(x, rgbcolor = mcolor) for x in outpaths]
        show(sum(lpaths)+nested+polys, axes = False, figsize = [5,5], xmin = -1, xmax = 1, ymin = -1, ymax =1)

Python
~~~~~~

.. sagecell::
    :lang: python

    import numpy as np
    import matplotlib.pyplot as plt
    import matplotlib.animation as animation

    fig = plt.figure()

    def f(x, y):
        return np.sin(x) + np.cos(y)

    x = np.linspace(0, 2 * np.pi, 120)
    y = np.linspace(0, 2 * np.pi, 100).reshape(-1, 1)

    im = plt.imshow(f(x, y), animated=True)

    def updatefig(*args):
        global x, y
        x += np.pi / 15.
        y += np.pi / 20.
        im.set_array(f(x, y))
        return im,

    ani = animation.FuncAnimation(fig, updatefig, interval=50, blit=True)
    plt.show()

Octave
~~~~~~

.. warning::
    Plotting in Octave is not working at the moment

.. sagecell::
    :lang: octave

    A = [ 1, 1, 2; 3, 5, 8; 13, 21, 34 ]
    B = rand (3, 2)
    A*B

Datacamp extensions
-------------------

Python
~~~~~~

.. datacamp::
    :lang: python
    :hidden:

    fdsa = 25*25

.. datacamp::
    :lang: python

    import numpy as np
    import matplotlib.pyplot as plt
    import matplotlib.animation as animation

    fig = plt.figure()

    def f(x, y):
        return np.sin(x) + np.cos(y)

    x = np.linspace(0, 2 * np.pi, 120)
    y = np.linspace(0, 2 * np.pi, 100).reshape(-1, 1)

    im = plt.imshow(f(x, y), animated=True)

    def updatefig(*args):
        global x, y
        x += np.pi / 15.
        y += np.pi / 20.
        im.set_array(f(x, y))
        return im,

    ani = animation.FuncAnimation(fig, updatefig, interval=50, blit=True)
    plt.show()

R
~~~

.. datacamp::
    :hidden:

    asdf <- 123412341234
    a <- 1


.. datacamp::
    :lang: r

    options(scipen=999)  # turn-off scientific notation like 1e+48
    library(ggplot2)
    theme_set(theme_bw())  # pre-set the bw theme.
    data("midwest", package = "ggplot2")

    gg <- ggplot(midwest, aes(x=area, y=poptotal)) + 
        geom_point(aes(col=state, size=popdensity)) + 
        geom_smooth(method="loess", se=F) + 
        xlim(c(0, 0.1)) + 
        ylim(c(0, 500000)) + 
        labs(subtitle="Area Vs Population", 
        y="Population", 
        x="Area", 
        title="Scatterplot", 
        caption = "Source: midwest")

    gg

Hoverrole Extension
-------------------
Þetta er texti um :hover:`stærðfræðigreiningu` og :hover:`afleiðujöfnur, deildajafna`. Fleiri hugtök: :hover:`heildi`, :hover:`ferill`, :hover:`vörpun`.

Auto-generated list of translated terms:

.. hoverlist::

Google Analytics Extension
----------------------------
This extension enables the use of Google Analytics by inserting the tracking code on each page (except the index) and by inserting your tracking ID inside conf.py you should be able to monitor the use of your site.

This extension also tracks how far users have scrolled on the page. When a new section is scrolled into view a Google Analytics event is fired. These events can be seen in real time in the Javascript console (Chrome: CTRL+Shift+I OR Options-> More Tools -> Developer Tools).