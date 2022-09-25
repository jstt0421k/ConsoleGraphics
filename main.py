# Console Graphics Module
# Developed for Python 3, by JS_TT0421.K

import math
import time

def render(v_printCoord_coordinatePlane):
    for v_printCoord_lv1 in range(0, len(v_printCoord_coordinatePlane)):
        for v_printCoord_lv2 in range(0, len(v_printCoord_coordinatePlane[0])):
            print(v_printCoord_coordinatePlane[v_printCoord_lv1][v_printCoord_lv2], end="")
        print()

"""
--> Deprecated :: Use new function, drawLine()
def line(v_line_startPointX, v_line_startPointY, v_line_endPointX, v_line_endPointY, v_line_coordinatePlane):
    if v_line_startPointX <= v_line_endPointX:
        if v_line_startPointX != v_line_endPointX:
            v_line_slope = (v_line_startPointY - v_line_endPointY) / (v_line_startPointX - v_line_endPointX)
        else:
            for v_line_lv2 in range(0, abs(v_line_startPointY - v_line_endPointY)):
                v_line_coordinatePlane[v_line_lv2 + min([v_line_startPointY, v_line_endPointY])][v_line_startPointX] = ' #'
            return v_line_coordinatePlane
        v_line_yIntercept = v_line_startPointY - v_line_slope * v_line_startPointX
        for v_line_lv1 in range(0, abs(v_line_startPointX - v_line_endPointX)):
            v_line_functionCoord = [v_line_startPointX + v_line_lv1, math.floor((v_line_startPointX + v_line_lv1) * v_line_slope + v_line_yIntercept)]
            if v_line_functionCoord[1] < len(v_line_coordinatePlane) and v_line_functionCoord[0] < len(v_line_coordinatePlane[0]):
                v_line_coordinatePlane[v_line_functionCoord[1]][v_line_functionCoord[0]] = ' #'
    else:
        line(v_line_endPointX, v_line_endPointY, v_line_startPointX, v_line_startPointY, v_line_coordinatePlane)
    return v_line_coordinatePlane
"""

def drawLine(v_drawLine_start, v_drawLine_end, v_drawLine_coordinatePlane):
    if v_drawLine_start[0] <= v_drawLine_end[0]:
        if v_drawLine_start[0] != v_drawLine_end[0]:
            v_drawLine_slope = (v_drawLine_start[1] - v_drawLine_end[1]) / (v_drawLine_start[0] - v_drawLine_end[0])
        else:
            for v_drawLine_lv2 in range(0, abs(v_drawLine_start[1] - v_drawLine_end[1])):
                v_drawLine_coordinatePlane [v_drawLine_lv2 + min([v_drawLine_start[1], v_drawLine_end[1]])][v_drawLine_start[0]] = ' #'
            return v_drawLine_coordinatePlane
        v_drawLine_yIntercept = v_drawLine_start[1] - v_drawLine_slope * v_drawLine_start[0]
        for v_drawLine_lv1 in range(0, abs(v_drawLine_start[0] - v_drawLine_end[0])):
            v_drawLine_functionCoord = [v_drawLine_start[0] + v_drawLine_lv1, math.floor((v_drawLine_start[0] + v_drawLine_lv1) * v_drawLine_slope + v_drawLine_yIntercept)]
            if v_drawLine_functionCoord[1] < len(v_drawLine_coordinatePlane) and v_drawLine_functionCoord[0] < len(v_drawLine_coordinatePlane[0]):
                v_drawLine_coordinatePlane[v_drawLine_functionCoord[1]][v_drawLine_functionCoord[0]] = ' #'
    else:
        drawLine(v_drawLine_end, v_drawLine_start, v_drawLine_coordinatePlane)
    return v_drawLine_coordinatePlane

"""
--> Deprecated :: Use new function, drawRect()
def rect(v_rect_cornerAX, v_rect_cornerAY, v_rect_cornerBX, v_rect_cornerBY, v_rect_cornerCX, v_rect_cornerCY, v_rect_cornerDX, v_rect_cornerDY, v_rect_coordinatePlane):
    v_rect_coordinatePlane = line(v_rect_cornerAX, v_rect_cornerAY, v_rect_cornerBX, v_rect_cornerBY, v_rect_coordinatePlane)
    v_rect_coordinatePlane = line(v_rect_cornerBX, v_rect_cornerBY, v_rect_cornerCX, v_rect_cornerCY, v_rect_coordinatePlane)
    v_rect_coordinatePlane = line(v_rect_cornerCX, v_rect_cornerCY, v_rect_cornerDX, v_rect_cornerDY, v_rect_coordinatePlane)
    v_rect_coordinatePlane = line(v_rect_cornerDX, v_rect_cornerDY, v_rect_cornerAX, v_rect_cornerAY, v_rect_coordinatePlane)
    return v_rect_coordinatePlane
"""

def drawRect(v_drawRect_corA, v_drawRect_corB, v_drawRect_corC, v_drawRect_corD, v_drawRect_coordinatePlane):
    v_drawRect_corList = [v_drawRect_corB, v_drawRect_corC, v_drawRect_corD, v_drawRect_corA]
    for v_drawRect_lv1 in range(0, 4):
        v_drawRect_coordinatePlane = drawLine(v_drawRect_corList[v_drawRect_lv1 - 1], v_drawRect_corList[v_drawRect_lv1], v_drawRect_coordinatePlane)
    return v_drawRect_coordinatePlane

"""
--> Error fix required :: Math Domain Error, probably complex number inpput in paraameter
def circle(v_circle_centerX, v_circle_centerY, v_circle_radius, v_circle_coordinatePlane):
   v_circle_cLb = [1, 1, -1, -1]
   for v_circle_lv1 in range(0, 4 * v_circle_radius):
       v_circle_functionCoord = [v_circle_lv1 // 4 + v_circle_centerX * v_circle_cLb[v_circle_lv1 % 2 + 1], v_circle_centerY + (math.sqrt(v_circle_radius ** 2 - (v_circle_lv1 // 4) ** 2 + 2 * v_circle_centerX * (v_circle_lv1 // 4) - v_circle_centerX ** 2)) * v_circle_cLb[v_circle_lv1 % 4]]
       v_circle_coordinatePlane[v_circle_functionCoord[1]][v_circle_functionCoord[0]] = ' #'
   return v_circle_coordinatePlane
--> Math Domain Error
"""

"""
def regPolygon(v_regPolygon_sideN, v_regPolygon_centerX, v_regPolygon_centerY, v_regPolygon_radius, v_regPolygon_coordinatePlane):
    v_regPolygon_cc = [v_regPolygon_centerX, v_regPolygon_centerY + v_regPolygon_radius]
    for v_regPolygon_lv1 in range(0, v_regPolygon_sideN):
        v_regPolygon_coordinatePlane = line(v_regPolygon_cc[0], v_regPolygon_cc[1], )
"""

def clear(v_sys_coordinatePlane):
    v_sys_coordinatePlane = []
    v_sys_cL = []
    v_sys_screenLengthX = 947
    v_sys_screenLengthY = 533
    for v_sys_lv3 in range(0, v_sys_screenLengthX):
        v_sys_cL.append(' #')
    v_sys_coordinatePlane.append(v_sys_cL)
    for v_sys_lv1 in range(1, v_sys_screenLengthY - 1):
        v_sys_xPlotList = []
        v_sys_xPlotList.append(' #')
        for v_sys_lv2 in range(1, v_sys_screenLengthX - 1):
            v_sys_xPlotList.append('  ')
        v_sys_xPlotList.append(' #')
        v_sys_coordinatePlane.append(v_sys_xPlotList)
    v_sys_coordinatePlane.append(v_sys_cL)
    return v_sys_coordinatePlane

v_sys_coordinatePlane = clear([])

# v_sys_lineStartX = int(input("ConsoleGraphics >> Line Start Point X Coordinate ? :: "))
# v_sys_lineStartY = int(input("ConsoleGraphics >> Line Start Point Y Coordinate ? :: "))
# v_sys_lineEndX = int(input("ConsoleGraphics >> Line End Point X Coordinate ? :: "))
# v_sys_lineEndY = int(input("ConsoleGraphics >> Line End Point Y Coordinate ? :: "))
"""
v_sys_coordinatePlane = drawLine([50, 50], [50, 100], v_sys_coordinatePlane)
v_sys_coordinatePlane = drawLine([100, 50], [100, 200], v_sys_coordinatePlane)
v_sys_coordinatePlane = drawLine([150, 50], [150, 300], v_sys_coordinatePlane)
v_sys_coordinatePlane = drawRect([200, 50], [300, 50], [300, 150], [200, 150], v_sys_coordinatePlane)
v_sys_coordinatePlane = drawRect([350, 50], [500, 50], [600, 150], [450, 150], v_sys_coordinatePlane)
"""
# v_sys_coordinatePlane = circle(750, 100, 50, v_sys_coordinatePlane)

for v_sys_lv3 in range(0, 5):
    corA = [35 + 60 * 3 * v_sys_lv3, 30]
    v_sys_rT = 1
    for v_sys_lv1 in range(0, 30):
        corB = [corA[0] + 20, corA[1]]
        corC = [corA[0] + 20, corA[1] + 20]
        corD = [corA[0], corA[1] + 20]
        v_sys_coordinatePlane = drawRect(corA, corB, corC, corD, v_sys_coordinatePlane)
        corA[0] += 3
        corA[1] += v_sys_lv1
        render(v_sys_coordinatePlane)
        time.sleep(v_sys_rT)
        # v_sys_coordinatePlane = clear(v_sys_coordinatePlane)
    if v_sys_lv3 != 4:
        for v_sys_lv1 in range(0, 30):
            corB = [corA[0] + 20, corA[1]]
            corC = [corA[0] + 20, corA[1] + 20]
            corD = [corA[0], corA[1] + 20]
            v_sys_coordinatePlane = drawRect(corA, corB, corC, corD, v_sys_coordinatePlane)
            corA[0] += 3
            corA[1] -= (29 - v_sys_lv1)
            render(v_sys_coordinatePlane)
            time.sleep(v_sys_rT)
            # v_sys_coordinatePlane = clear(v_sys_coordinatePlane)

render(v_sys_coordinatePlane)