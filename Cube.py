 import pygame
    from OpenGL.GL import *
    from OpenGL.GLU import *
    screen = pygame.display.set_mode((640,480),pygame.HWSURFACE|pygame.DOUBLEBUF|pygame.OPENGL)
     
    clock = pygame.time.Clock()
     
    glClearColor(0,0,0,1)
    glViewport(0, 0, 640, 480)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(65, 640/480., .1, 1000)
    glMatrixMode(GL_MODELVIEW)
    r=0
    glEnable(GL_DEPTH_TEST)
    while True:
        r+=3
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                raise SystemExit
     
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        glTranslated(0,0,-5)
        glRotated(r,1,0,0)
        glRotated(r,0,1,0)
        glRotated(r,0,0,1)
        glBegin(GL_QUADS)
        glColor4d(1,1,0,1)
        glVertex3d(-1,-1,-1)
        glVertex3d(+1,-1,-1)
        glVertex3d(+1,+1,-1)
        glVertex3d(-1,+1,-1)
        glColor4d(1,0,1,1)
        glVertex3d(-1,-1,+1)
        glVertex3d(+1,-1,+1)
        glVertex3d(+1,+1,+1)
        glVertex3d(-1,+1,+1)
        glColor4d(0,1,1,1)
        glVertex3d(-1,-1,-1)
        glVertex3d(-1,+1,-1)
        glVertex3d(-1,+1,+1)
        glVertex3d(-1,-1,+1)
        glColor4d(0,1,0,1)
        glVertex3d(+1,-1,-1)
        glVertex3d(+1,+1,-1)
        glVertex3d(+1,+1,+1)
        glVertex3d(+1,-1,+1)
        glColor4d(1,0,0,1)
        glVertex3d(-1,-1,-1)
        glVertex3d(+1,-1,-1)
        glVertex3d(+1,-1,+1)
        glVertex3d(-1,-1,+1)
        glColor4d(0,0,1,1)
        glVertex3d(-1,+1,-1)
        glVertex3d(+1,+1,-1)
        glVertex3d(+1,+1,+1)
        glVertex3d(-1,+1,+1)
        glEnd()
        pygame.display.flip()
