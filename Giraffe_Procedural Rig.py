import maya.cmds as cmd

locs4 = ["NECK_LOC","SPINE_LOC","HIP_LOC"]
jnts4 = ["NECK_JNT","SPINE_JNT","HIP_JNT"]
cons4 = ["NECK_CON","SPINE_CON","HIP_CON"]
geom4 = ["NECK_GEO","SPINE_GEO","HIP_GEO"]
    
locs5 = ["HIP_LOC","R_B_upperleg_LOC","R_B_knee_LOC","R_B_carpus_LOC","R_B_hoof_LOC"]
locs15 = ["R_B_upperleg_LOC","R_B_knee_LOC","R_B_hoof_LOC"]
jnts5 = ["HIP_JNT00","R_B_upperleg_JNT","R_B_knee_JNT","R_B_carpus_JNT","R_B_hoof_JNT"]  
jnts15 = ["R_B_upperleg_JNT","R_B_knee_JNT","R_B_hoof_JNT"]
geom5 = ["R_B_upperleg_GEO","R_B_knee_GEO","R_B_hoof_GEO"]
cons5 = ["HIP_CON","R_B_upperleg_CON","R_B_knee_CON","R_B_carpus_CON","R_B_hoof_CON"]

locs6 = ["HIP_LOC","L_B_upperleg_LOC","L_B_knee_LOC","L_B_carpus_LOC","L_B_hoof_LOC"]
locs16 = ["L_B_upperleg_LOC","L_B_knee_LOC","L_B_hoof_LOC"]
jnts6 = ["HIP_JNT0","L_B_upperleg_JNT","L_B_knee_JNT","L_B_carpus_JNT","L_B_hoof_JNT"]
jnts16 = ["L_B_upperleg_JNT","L_B_knee_JNT","L_B_hoof_JNT"]
cons6 = ["HIP_CON","L_B_upperleg_CON","L_B_knee_CON","L_B_carpus_CON","L_B_hoof_CON"]
geom6 = ["L_B_upperleg_GEO","L_B_knee_GEO","L_B_hoof_GEO"]

locs7 = ["SPINE_LOC","TAIL_LOC","TAIL2_LOC","TAIL3_LOC","TAIL4_LOC"]
jnts7 = ["SPINE0_JNT","TAIL_JNT","TAIL2_JNT","TAIL3_JNT","TAIL4_JNT"]
cons7 = ["SPINE_CON","TAIL_CON","TAIL2_CON","TAIL3_CON","TAIL4_CON"]
geom17 = ["SPINE_GEO","TAIL11_GEO","TAIL12_GEO","TAIL13_GEO","TAIL14_GEO"]


##### Locators ###
      

def createLocators():
    if cmd.objExists("Global_LOC"):
        print "Alreay Exists"
    else:
        cmd.group(em=True, name = "Global_LOC") # creates locator
     
     
        
    #NECK
    neck = cmd.spaceLocator(n = "NECK_LOC")
    cmd.parent(neck, "Global_LOC")
    cmd.move(-6,18,0,neck)

    
    #NECK2
    neck2 = cmd.spaceLocator(n = "NECK2_LOC")
    cmd.parent(neck2, "NECK_LOC")
    cmd.move(-9,19.5,0,neck2)
    
    #NECK3
    neck3 = cmd.spaceLocator(n = "NECK3_LOC")
    cmd.parent(neck3, "NECK2_LOC")
    cmd.move(-10.5,22.5,0,neck3)
    
       
    #HEAD
    head = cmd.spaceLocator(n = "HEAD_LOC")
    cmd.parent(head, "NECK3_LOC" )
    cmd.move(-12.5,26,0,head)
    
    #MOUTH21
    mouth = cmd.spaceLocator(n = "MOUTH_LOC")
    cmd.parent(mouth, "HEAD_LOC" )
    cmd.move(-16,24,0,mouth)
    
    
    #SPINE
    spine = cmd.spaceLocator(n = "SPINE_LOC")
    cmd.move(1,14.5,0,spine) 
    cmd.parent(spine, "NECK_LOC")
    
    #TAIL
    tail = cmd.spaceLocator(n = "TAIL_LOC")
    cmd.move(2.5,14,0,tail)
    cmd.parent(tail, "SPINE_LOC")
    
    #TAIL2
    tail2 = cmd.spaceLocator(n = "TAIL2_LOC")
    cmd.move(3,12.5,0,tail2)
    cmd.parent(tail2, "TAIL_LOC")
    
    #TAIL3
    tail3 = cmd.spaceLocator(n = "TAIL3_LOC")
    cmd.move(3,9.5,0,tail3)
    cmd.parent(tail3, "TAIL2_LOC")
    
    #TAIL4
    tail4 = cmd.spaceLocator(n = "TAIL4_LOC")
    cmd.move(2.5,7.5,0,tail4)
    cmd.parent(tail4, "TAIL3_LOC")
    

    
    #HIP
    hip = cmd.spaceLocator(n = "HIP_LOC")
    cmd.move(1.5,12.5,0,hip)
    cmd.parent(hip, "SPINE_LOC")
    
    #LEFT_SCAP
    L_scap = cmd.spaceLocator(n = "L_SCAP_LOC")
    cmd.parent(L_scap, "NECK_LOC")
    cmd.move(-7,14.5,1.5,L_scap)
    
    #RIGHT_SCAP
    R_scap = cmd.spaceLocator(n = "R_SCAP_LOC")
    cmd.parent(R_scap, "NECK_LOC") 
    cmd.move(-7,14.5,-1.5,R_scap) 
    
    
    #LEFT_FRONT_LEG
    
    L_F_upperleg = cmd.spaceLocator(n = "L_F_upperleg_LOC")
    cmd.move(-5.7,11, 2,L_F_upperleg)
 
    cmd.parent(L_F_upperleg, "L_SCAP_LOC")
    
    L_F_knee = cmd.spaceLocator(n = "L_F_knee_LOC")
    cmd.move(-5.5,7, 2,L_F_knee)
    cmd.parent(L_F_knee, "L_F_upperleg_LOC")
    
    L_F_carpus = cmd.spaceLocator(n = "L_F_carpus_LOC")
    cmd.move(-4.6,1.5, 2,L_F_carpus)
    cmd.parent(L_F_carpus, "L_F_knee_LOC")
    
    L_F_hoof = cmd.spaceLocator(n = "L_F_hoof_LOC")
    cmd.move(-5.5,0, 2,L_F_hoof)
    cmd.parent(L_F_hoof, "L_F_carpus_LOC")    
 
    #LEFT_BACK_LEG
    
    L_B_upperleg = cmd.spaceLocator(n = "L_B_upperleg_LOC")
    cmd.move(0,10.5, 2,L_B_upperleg)
    cmd.parent(L_B_upperleg, "HIP_LOC")
    
    L_B_knee = cmd.spaceLocator(n = "L_B_knee_LOC")
    cmd.move(1,7, 2,L_B_knee)
    cmd.parent(L_B_knee, "L_B_upperleg_LOC")
    
    
    L_B_carpus = cmd.spaceLocator(n = "L_B_carpus_LOC")
    cmd.move(0.5,1.5, 2,L_B_carpus)
    cmd.parent(L_B_carpus, "L_B_knee_LOC")    
    
    
    L_B_hoof = cmd.spaceLocator(n = "L_B_hoof_LOC")
    cmd.move(0.2,0, 2,L_B_hoof)
    cmd.parent(L_B_hoof, "L_B_carpus_LOC")
    
    
    #RIGHT_FRONT_LEG
    
    R_F_upperleg = cmd.spaceLocator(n = "R_F_upperleg_LOC")
    cmd.move(-5.7,11,-2,R_F_upperleg)
    cmd.parent(R_F_upperleg, "R_SCAP_LOC")
    
    R_F_knee = cmd.spaceLocator(n = "R_F_knee_LOC")
    cmd.move(-5.5,7, -2,R_F_knee)
    cmd.parent(R_F_knee, "R_F_upperleg_LOC")
    
    R_F_carpus = cmd.spaceLocator(n = "R_F_carpus_LOC")
    cmd.move(-4.6,1.5, -2,R_F_carpus)
    cmd.parent(R_F_carpus, "R_F_knee_LOC")    
    
    R_F_hoof = cmd.spaceLocator(n = "R_F_hoof_LOC")
    cmd.move(-4.5,0, -2,R_F_hoof)
    cmd.parent(R_F_hoof, "R_F_carpus_LOC")
 
    #RIGHT_BACK_LEG
    
    R_B_upperleg = cmd.spaceLocator(n = "R_B_upperleg_LOC")
    cmd.move(0,10.5, -2,R_B_upperleg) 
    cmd.parent(R_B_upperleg, "HIP_LOC")
    
    R_B_knee = cmd.spaceLocator(n = "R_B_knee_LOC")
    cmd.move(1,7, -2,R_B_knee)
    cmd.parent(R_B_knee, "R_B_upperleg_LOC")

    R_B_carpus = cmd.spaceLocator(n = "R_B_carpus_LOC")
    cmd.move(0.5,1.5, -2,R_B_carpus)
    cmd.parent(R_B_carpus, "R_B_knee_LOC") 
        
    R_B_hoof = cmd.spaceLocator(n = "R_B_hoof_LOC")
    cmd.move(-0.2,0, -2,R_B_hoof)
    cmd.parent(R_B_hoof, "R_B_carpus_LOC")
    
    
    
#### JOINTS AND CONTROLS ####

def rig():
    
    if cmd.objExists("RIG"):
        print "Alreay Exists"
    else:
        cmd.group(em=True, name = "RIG") 
        
                
def controls():
    
    if cmd.objExists("Global_CON"):
        print "Alreay Exists"
    else:
        cmd.group(em=True, name = "Global_CON") 
        cmd.group(em=True, name = "NECK_GRP")
        cmd.group(em=True, name = "SPINE_GRP")
        
        cmd.group(em=True, name = "R_SCAP_GRP") 
        cmd.group(em=True, name = "L_SCAP_GRP")  
        
        cmd.group(em=True, name = "R_B_leg_GRP ")
        cmd.group(em=True, name = "L_B_leg_GRP ")
        cmd.group(em=True, name = "TAIL_GRP ")
        
        cmds.circle( nr=(0, 1, 0), c=(-0.25,0,0), name="G_CON")
        cmd.parent('G_CON', 'Global_CON')
        cmds.scale( 10, 10, 10 )
             
    
       
def createneckJoints1():
    
    locs1 = ["NECK_LOC","NECK2_LOC","NECK3_LOC", "HEAD_LOC","MOUTH_LOC" ]
    jnts1 = ["NECK_JNT","NECK2_JNT","NECK3_JNT","HEAD_JNT","MOUTH_JNT"]
    cons1 = ["NECK_CON","NECK2_CON","NECK3_CON","HEAD_CON","MOUTH_CON"]
    geom1 = ["NECK1_GEO","NECK2_GEO","NECK3_GEO","HEAD_GEO","MOUTH_GEO"]
    
    
    if cmd.objExists("NECK_JNT_GRP"):
        print "Alreay Exists"
    else:
        cmd.group(em=True, name = "NECK_JNT_GRP")
        cmds.xform( cp=True)  
        cmd.parent('NECK_JNT_GRP', 'RIG')
        


    ax = 0
    ay = 0
    az = 0
    
    
    for i in range(len(locs1)): #creates joints
        each = locs1[i]
        print(each)
        ax += cmd.getAttr(each + '.translateX')
        ay += cmd.getAttr(each + '.translateY')
        az += cmd.getAttr(each + '.translateZ')
        print(str(ax) +" " + str(ay) + " " + str(az) )
        cmd.joint(p=(ax,ay,az),a=True, name=jnts1[i])

        
    ax = 0
    ay = 0
    az = 0
    
       
    for i in range(len(locs1)): #creates controls
        each = locs1[i]
        ax += cmd.getAttr(each + '.translateX')
        ay += cmd.getAttr(each + '.translateY')
        az += cmd.getAttr(each + '.translateZ')
        cmds.circle( nr=(0, 1, 0), c=(ax,ay,az), name=cons1[i] ) 
        cmds.xform( cp=True)
        cmds.scale( 2, 2, 2.5 )
        cmd.parentConstraint(cons1[i], jnts1[i])
        cmds.bindSkin( geom1[i], jnts1[i] )
     
       
    cmd.parent(cons1[0], 'NECK_GRP') 
        
    for i in range(len(cons1)-1):
        loop = cons1[i+1]
        cmd.parent(loop, cons1[i])

        
    cmd.parent('NECK_GRP', 'Global_CON')
    
            
         
  
  
      

def createR_scap():  

    locs2 = ["NECK_LOC","R_SCAP_LOC","R_F_upperleg_LOC","R_F_knee_LOC","R_F_carpus_LOC","R_F_hoof_LOC"]
    locs12 = ["R_SCAP_LOC","R_F_upperleg_LOC","R_F_knee_LOC","R_F_hoof_LOC"]
    jnts2 = ["NECK0_JNT","R_SCAP_JNT","R_F_upperleg_JNT","R_F_knee_JNT","R_F_carpus_JNT","R_F_hoof_JNT"]
    jnts12 = ["R_SCAP_JNT","R_F_upperleg_JNT","R_F_knee_JNT","R_F_hoof_JNT"]   
    geom2 = ["R_SCAP_GEO","R_F_upperleg_GEO","R_F_knee_GEO","R_F_hoof_GEO"]  
    cons2 = ["NECK_CON","R_SCAP_CON","R_F_upperleg_CON","R_F_knee_CON","R_F_carpus_CON","R_F_hoof_CON"]

    
    if cmd.objExists("R_SCAP_JNT_GRP"):
        print "Alreay Exists"
    else:
        cmd.group(em=True, name = "R_SCAP_JNT_GRP")
        cmd.parent('R_SCAP_JNT_GRP', 'NECK_JNT_GRP')
        
        

    ax = 0
    ay = 0
    az = 0        
        
        
    for j in range(len(locs2)):
        each = locs2[j]
        ax += cmd.getAttr(each + '.translateX')
        ay += cmd.getAttr(each + '.translateY')
        az += cmd.getAttr(each + '.translateZ')
        cmd.joint(p=(ax,ay,az),a=True, name=jnts2[j])
        print(str(ax) +" " + str(ay) + " " + str(az) )
        
        
    ax = -6
    ay = 18
    az = 0 

   
    for i in range(len(locs2)-1): #creates controls
        each = locs2[i+1]
        ax += cmd.getAttr(each + '.translateX')
        ay += cmd.getAttr(each + '.translateY')
        az += cmd.getAttr(each + '.translateZ')
        cmds.circle( nr=(0, 1, 0), c=(ax,ay,az), name=cons2[i+1])
         
        cmds.xform( cp=True)
        cmds.scale( 1.5, 1, 1 )
        cmd.parentConstraint(cons2[i], jnts2[i])
        
        
    for i in range(len(locs12)):       
        cmds.bindSkin( geom2[i], jnts2[i] )
        
 
    cmd.parent(cons2[1], 'R_SCAP_GRP') 
        
        
    for i in range(len(cons2)-1):
        loop = cons2[i+1]
        cmd.parent(loop, cons2[i])     
               
    cmd.parent('R_SCAP_GRP', 'Global_CON')
    

    

        

        
def createL_scap():  
    locs13 = ["L_SCAP_LOC","L_F_upperleg_LOC","L_F_knee_LOC","L_F_hoof_LOC"]
    locs3 = ["NECK_LOC","L_SCAP_LOC","L_F_upperleg_LOC","L_F_knee_LOC","L_F_carpus_LOC","L_F_hoof_LOC"]
    jnts3 = ["NECK00_JNT","L_SCAP_JNT","L_F_upperleg_JNT","L_F_knee_JNT","L_F_carpus_JNT","L_F_hoof_JNT"]
    jnts13 = ["L_SCAP_JNT","L_F_upperleg_JNT","L_F_knee_JNT","L_F_hoof_JNT"]
    cons3 = ["NECK_CON","L_SCAP_CON","L_F_upperleg_CON","L_F_knee_CON","L_F_carpus_CON","L_F_hoof_CON"]
    geom3 = ["L_SCAP_GEO","L_F_upperleg_GEO","L_F_knee_GEO","L_F_hoof_GEO"]

    
    if cmd.objExists("L_SCAP_JNT_GRP"):
        print "Alreay Exists"
    else:
        cmd.group(em=True, name = "L_SCAP_JNT_GRP")
        cmd.parent('L_SCAP_JNT_GRP','NECK_JNT_GRP')
 
    ax = 0
    ay = 0
    az = 0        
        
        
    for k in range(len(locs3)):
        each = locs3[k]
        ax += cmd.getAttr(each + '.translateX')
        ay += cmd.getAttr(each + '.translateY')
        az += cmd.getAttr(each + '.translateZ')
        cmd.joint(p=(ax,ay,az),a=True, name=jnts3[k])
        
    ax = -6
    ay = 18
    az = 0 
        
    for i in range(len(locs3)-1): #creates controls
        each = locs3[i+1]
        ax += cmd.getAttr(each + '.translateX')
        ay += cmd.getAttr(each + '.translateY')
        az += cmd.getAttr(each + '.translateZ')
        cmds.circle( nr=(0, 1, 0), c=(ax,ay,az), name=cons3[i+1])        
        cmds.xform( cp=True)
        cmds.scale( 1.5, 1, 1 )
        cmd.parentConstraint(cons3[i], jnts3[i]) 
   
    for i in range(len(locs13)):       
        cmds.bindSkin( geom3[i], jnts3[i] )        
        
    cmd.parent(cons3[1], 'L_SCAP_GRP') 
        
        
    for i in range(len(cons3)-1):
        loop = cons3[i+1]
        cmd.parent(loop, cons3[i])    
                
        
    cmd.parent('L_SCAP_GRP', 'Global_CON') 
    

  
        
        
def createspine(): 
    locs4 = ["NECK_LOC","SPINE_LOC","HIP_LOC"]
    jnts4 = ["NECK000_JNT","SPINE_JNT","HIP_JNT"]
    cons4 = ["NECK_CON","SPINE_CON","HIP_CON"] 
    
    if cmd.objExists("SPINE_JNT_GRP"):
        print "Alreay Exists"
    else:
        cmd.group(em=True, name = "SPINE_JNT_GRP")
        cmd.parent('SPINE_JNT_GRP', 'NECK_JNT_GRP')
 
 
    ax = 0
    ay = 0
    az = 0        
        
        
    for l in range(len(locs4)):
        each = locs4[l]

        ax += cmd.getAttr(each + '.translateX')
        ay += cmd.getAttr(each + '.translateY')
        az += cmd.getAttr(each + '.translateZ')

        cmd.joint(p=(ax,ay,az),a=True, name=jnts4[l])
       
        
        
def createspinecon(): 
    locs4 = ["NECK_LOC","SPINE_LOC","HIP_LOC"]
    jnts4 = ["NECK000_JNT","SPINE_JNT","HIP_JNT"]
    cons4 = ["NECK_CON","SPINE_CON","HIP_CON"] 
    
    ax = -6
    ay = 18
    az = 0      
             
        
    for i in range(len(locs4)-1): #creates controls
        each = locs4[i+1]
        ax += cmd.getAttr(each + '.translateX')
        ay += cmd.getAttr(each + '.translateY')
        az += cmd.getAttr(each + '.translateZ')
        cmds.circle( nr=(1, 0, 0), c=(ax,ay,az), name=cons4[i+1]) 
        cmds.xform( cp=True) 
        cmds.scale( 2, 2, 4.5 )
        cmd.parentConstraint(cons4[i], jnts4[i])
        
        
    for i in range(len(locs4)):       
        cmds.bindSkin( geom4[1], jnts4[1] ) 
    
    #cmd.parentConstraint(cons4[1], jnts4[1]) 
    cmd.parent(cons4[1], 'SPINE_GRP')
    
    for i in range(len(cons4)-2):
        loop = cons4[i+2]
        cmd.parent(loop, cons4[1])        
        
     
        
    cmd.parent('SPINE_GRP', 'Global_CON')

                
        
        
        
        

def createR_B_legjoints():

    
    if cmd.objExists("R_B_legjoints_JNT_GRP"):
        print "Alreay Exists"
    else:
        cmd.group(em=True, name = "R_B_legjoints_JNT_GRP")
        cmd.parent('R_B_legjoints_JNT_GRP', 'SPINE_JNT_GRP')
 
  
    ax = 0
    ay = 0
    az = 0 
    
    for l in range(len(locs4)-1):
        each = locs4[l]

        ax += cmd.getAttr(each + '.translateX')
        ay += cmd.getAttr(each + '.translateY')
        az += cmd.getAttr(each + '.translateZ')

  
        
    for m in range(len(locs5)):
        each = locs5[m]

        ax += cmd.getAttr(each + '.translateX')
        ay += cmd.getAttr(each + '.translateY')
        az += cmd.getAttr(each + '.translateZ')

        cmd.joint(p=(ax,ay,az),a=True, name=jnts5[m]) 
        
        
    ax = 1.5
    ay = 12.5
    az = 0           
                
        
    for i in range(len(locs5)-1): #creates controls
        each = locs5[i+1]
        ax += cmd.getAttr(each + '.translateX')
        ay += cmd.getAttr(each + '.translateY')
        az += cmd.getAttr(each + '.translateZ')
        cmds.circle( nr=(0, 1, 0), c=(ax,ay,az), name=cons5[i+1]) 
        cmds.xform( cp=True)
        print('find')
        print(str(ax) +" " + str(ay) + " " + str(az) ) 
        cmd.parentConstraint(cons5[i], jnts5[i])
        
        
    for i in range(len(locs15)):       
        cmds.bindSkin( geom5[i], jnts15[i] )           
        
        
    cmd.parent(cons5[1], 'R_B_leg_GRP') 
        
        
    for i in range(len(cons5)-1):
        loop = cons5[i+1]
        cmd.parent(loop, cons5[i])          
                  

    cmd.parent('R_B_leg_GRP', 'Global_CON')    

    
    
    
        
                            
def createL_B_legjoints():  
    
    if cmd.objExists("L_B_legjoints_JNT_GRP"):
        print "Alreay Exists"
    else:
        cmd.group(em=True, name = "L_B_legjoints_JNT_GRP")
        cmd.parent('L_B_legjoints_JNT_GRP', 'SPINE_JNT_GRP')
 
  
    ax = 0
    ay = 0
    az = 0        
        
    for l in range(len(locs4)-1):
        each = locs4[l]
        print(each)
        ax += cmd.getAttr(each + '.translateX')
        ay += cmd.getAttr(each + '.translateY')
        az += cmd.getAttr(each + '.translateZ')
        print(str(ax) +" " + str(ay) + " " + str(az) )

      
                     
                
    for n in range(len(locs6)):
        each = locs6[n]
        print(each)
        ax += cmd.getAttr(each + '.translateX')
        print(ax)
        ay += cmd.getAttr(each + '.translateY')
        az += cmd.getAttr(each + '.translateZ')
        print(str(ax) +" " + str(ay) + " " + str(az) )

        cmd.joint(p=(ax,ay,az),a=True, name=jnts6[n]) 
        
        
    ax = 1.5
    ay = 12.5
    az = 0          
              
    for i in range(len(locs6)-1): #creates controls
        each = locs6[i+1]
        ax += cmd.getAttr(each + '.translateX')
        ay += cmd.getAttr(each + '.translateY')
        az += cmd.getAttr(each + '.translateZ')
        cmds.circle( nr=(0, 1, 0), c=(ax,ay,az), name=cons6[i+1]) 
        cmds.xform( cp=True) 
        cmd.parentConstraint(cons6[i], jnts6[i]) 
        
    for i in range(len(locs16)):       
        cmds.bindSkin( geom6[i], jnts16[i] )         
        
                
                

    cmd.parent(cons6[1], 'L_B_leg_GRP') 
        
        
    for i in range(len(cons6)-1):
        loop = cons6[i+1]
        cmd.parent(loop, cons6[i]) 
        
    cmd.parent('L_B_leg_GRP', 'HIP_JNT')

        
        
def createtailjoints():
    
    if cmd.objExists("TAIL_JNT_GRP"):
        print "Alreay Exists"
    else:
        cmd.group(em=True, name = "TAIL_JNT_GRP") 
        cmd.parent('TAIL_JNT_GRP', 'RIG')
        
      

    print(locs7)
    ax = 0
    ay = 0
    az = 0
    
    for l in range(len(locs4)-2):
        each = locs4[l]
        print(each)
        ax += cmd.getAttr(each + '.translateX')
        ay += cmd.getAttr(each + '.translateY')
        az += cmd.getAttr(each + '.translateZ')
        print(str(ax) +" " + str(ay) + " " + str(az) )
            
    
    
    for r in range(len(locs7)):
        each = locs7[r]
        print(each)
        ax += cmd.getAttr(each + '.translateX')
        ay += cmd.getAttr(each + '.translateY')
        az += cmd.getAttr(each + '.translateZ')
        print(str(ax) +" " + str(ay) + " " + str(az) )
        cmd.joint(p=(ax,ay,az),a=True, name=jnts7[r])

    ax = 1
    ay = 14.5
    az = 0           
              
            
    for i in range(len(locs7)-1): #creates controls
        each = locs7[i+1]
        ax += cmd.getAttr(each + '.translateX')
        ay += cmd.getAttr(each + '.translateY')
        az += cmd.getAttr(each + '.translateZ')
        cmds.circle( nr=(0, 1, 0), c=(ax,ay,az), name=cons7[i+1]) 
        cmds.xform( cp=True) 
        
        
    for i in range(len(locs7)):        
        cmd.parentConstraint(cons7[i], jnts7[i])  
        
        
    for i in range(len(locs7)-1):       
        cmds.bindSkin( geom17[i+1], jnts7[i+1] )         

    cmd.parent(cons7[1], 'TAIL_GRP') 
        
        
    for i in range(len(cons7)-1):
        loop = cons7[i+1]
        cmd.parent(loop, cons7[i]) 
                        
    cmd.parent('TAIL_GRP', 'Global_CON') 

cmds.scaleConstraint( 'Global_CON', 'GIRAFFE_GEO' )


createLocators()
rig()
controls()
createneckJoints1()
createspine()
createspinecon()

createR_scap()
createL_scap()      

createR_B_legjoints()
createL_B_legjoints()
createtailjoints()




