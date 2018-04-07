import pymel.core as pm

def scale_hierarchy():
    # Select the entire hierarchy of your current selection and store everything in a list
    pm.select(hi=True, r=True)
    selected = pm.ls(sl=True)
    
    # If the ScaleMe group does not exist, create it
    if not pm.objExists('ScaleMe'):
        # Create the group that you will scale to resize your items
        scale_me = pm.createNode('transform', n='ScaleMe')
        
        # Iterate through all items, create a locator for each and set the locators to the items...
        # then reverse the constraint relationship so that the locators drive the items. Make all locators children of the ScaleMe group
        for s in selected:
            loc = pm.spaceLocator(n=s+'_ScaleLoc')
            p_con = pm.pointConstraint(s, loc)
            o_con = pm.orientConstraint(s, loc)
            pm.delete(p_con, o_con) 
            pm.pointConstraint(loc, s)
            pm.orientConstraint(loc, s)
            pm.parent(loc, scale_me)
    else:
        # Grabbing all applicable joints using the locators attached to them
        items_to_key = [item.split('_ScaleLoc')[0] for item in pm.listRelatives('ScaleMe', c=True)]

        # Setting a keyframe on each item, then deleting the ScaleMe group (which deletes all constraints with it)
        for item in items_to_key:
            pm.setKeyframe(item, at=['tx','ty', 'tz', 'rx', 'ry', 'rz'])
        pm.delete('ScaleMe')
        
        # Gets rid of all keys on the items that were just resized. You can comment this out if you want to keep the keyframes.
        for item in items_to_key:
            pm.cutKey(item)

scale_hierarchy()