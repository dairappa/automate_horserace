craneButton = Pattern("craneButton.png").targetOffset(-211,728)
craneSpeedNormal = "craneSpeedNormal.png"
craneSpeedFast = "craneSpeedFast.png"


reg = Region(0,0,601,1111)

reg.drag(craneButton)

#sleep(1.2) normal
#sleep(0.4) fast
sleep(0.1) super fast

reg.dropAt(craneButton)