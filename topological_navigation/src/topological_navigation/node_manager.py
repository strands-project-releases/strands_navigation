#!/usr/bin/env python

import sys
import rospy
import math
import tf
import actionlib
from threading import Timer


import std_msgs.msg
from geometry_msgs.msg import Pose
from geometry_msgs.msg import Point

from visualization_msgs.msg import *
from interactive_markers.interactive_marker_server import *

from strands_navigation_msgs.msg import TopologicalNode
from topological_navigation.topological_map import *
from strands_navigation_msgs.msg import TopologicalMap

import topological_navigation.msg


class node_manager(object):

    def __init__(self, map_name) :
        self.in_feedback=False
        #self.timer = Timer(1.0, self.timer_callback)
        self._node_server = InteractiveMarkerServer(map_name+"_add_rm_node")
        rospy.loginfo(" ... Init done")


        
    def update_map(self, msg) :
        print "updating node controllers..."
        self.topo_map = topological_map(msg.name, msg=msg)
        self._node_server.clear()
        self._node_server.applyChanges()
        self.create_marker()
        


    def makeEmptyMarker(self, dummyBox=True ) :
        int_marker = InteractiveMarker()
        int_marker.header.frame_id = "/base_link"
        int_marker.scale = 1
        return int_marker


    def makeBox(self, msg ):
        marker = Marker()

        marker.type = Marker.CUBE
        marker.scale.x = msg.scale * 0.125
        marker.scale.y = msg.scale * 0.25
        marker.scale.z = msg.scale * 0.1
        marker.lifetime.secs = 3
        marker.color.r = 0.1
        marker.color.g = 0.8
        marker.color.b = 0.1
        marker.color.a = 1.0
        return marker


    def create_marker(self) :
      
        marker = self.makeEmptyMarker()
        marker.name = "add_node"
        marker.description = "add_node"

        control = InteractiveMarkerControl()
    
        control.interaction_mode = InteractiveMarkerControl.BUTTON
        control.always_visible = True

        control.markers.append( self.makeBox( marker ) )
        marker.controls.append(control)
    
        self._node_server.insert(marker, self.feedback_cb)
        self._node_server.applyChanges()

        pos=Pose()
        pos.position.x=0.0
        pos.position.y=0.0
        pos.position.z=1.9
        pos.orientation.x=0.0
        pos.orientation.y=0.0
        pos.orientation.z=0.0
        pos.orientation.w=0.0

        self._node_server.setPose( marker.name, pos )
        self._node_server.applyChanges()



    def feedback_cb(self, feedback):
        if not self.in_feedback :
            self.in_feedback=True

            try:
                current = rospy.wait_for_message('/current_node', std_msgs.msg.String, timeout=10.0)
            except rospy.ROSException :
                rospy.logwarn("Failed to get current node")
                return
            
            print current.data
            if current.data == 'none':
                try:
                    pos = rospy.wait_for_message('/robot_pose', Pose, timeout=10.0)
                except rospy.ROSException :
                    rospy.logwarn("Failed to get robot pose")
                    return
                
                lnames=[]
                for i in self.topo_map.nodes :
                     if i.name.startswith('WayPoint') :
                         nam = i.name.strip('WayPoint')
                         lnames.append(int(nam))
                
                lnames.sort()
                print "used names:"
                for j in lnames :
                    print j
                
                print "Chosen name!!!!!!"
                if lnames:
                    nodname = 'WayPoint%d'%(int(lnames[-1])+1)
                else :
                    nodname = 'WayPoint1'
                print nodname
                #self.topo_map = topological_map(pointset)     
                self.topo_map.add_node(nodname,8.0, pos, 'move_base')
            
                map_update = rospy.Publisher('/update_map', std_msgs.msg.Time)        
                map_update.publish(rospy.Time.now())            
            
            else:
                rospy.loginfo("I will NOT add a node within the influence area of another! Solve this and try again!")
            
            
            self.timer = Timer(1.0, self.timer_callback)      
            self.timer.start()


    def timer_callback(self) :
        self.in_feedback = False
    
    def clear():
        self._node_server.clear()
        self._node_server.applyChanges()

        
    def __del__(self):
        del self._node_server
