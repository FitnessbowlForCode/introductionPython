import math

def distanceVertical(gpstrack):
    asc = 0.0
    desc = 0.0
    diffList = []

    for i in range(len(gpstrack)-1):
        z1 = gpstrack[i][2]
        z2 = gpstrack[i+1][2]
        diff = z2 - z1
        if diff > 0:
            asc += diff
        elif diff < 0:
            desc += abs(diff) 
    diffList.append(asc)
    diffList.append(desc)
    return tuple(diffList)

def distanceHorizontal(gpstrack):
    total_dist = 0.0
    exponent = 2

    for i in range(len(gpstrack)-1):
        p1 = gpstrack[i]
        p2 = gpstrack[i+1]
        diff_x = p2[0] - p1[0]
        diff_y = p2[1] - p1[1]
        segment_dist = math.sqrt(diff_x**exponent + diff_y**exponent)
        total_dist += segment_dist
    return total_dist

def plan(gpstrack):
    vert_data = distanceVertical(gpstrack)
    asc = vert_data[0]
    desc = vert_data[1]
    dist = distanceHorizontal(gpstrack)

    speed_hor = 4000.0  
    speed_asc = 300.0   
    speed_desc = 500.0  

    t_hor = dist / speed_hor
    t_asc = asc / speed_asc
    t_desc = desc / speed_desc

    t_vert_total = t_asc + t_desc

    if t_hor > t_vert_total:
        total_hours = t_hor + (t_vert_total * 0.5)
    else:
        total_hours = t_vert_total + (t_hor * 0.5)

    return total_hours * 60

def calcSpeed(gpstrack):
    if len(gpstrack) < 2:
        return 0.0
    
    total_dist_3d = 0.0
    
    has_explicit_time = (len(gpstrack[0]) == 4)
    
    for i in range(len(gpstrack)-1):
        p1 = gpstrack[i]
        p2 = gpstrack[i+1]
        
        diff_x = p2[0] - p1[0]
        diff_y = p2[1] - p1[1]
        diff_z = p2[2] - p1[2]
        
        segment_dist = math.sqrt(diff_x**2 + diff_y**2 + diff_z**2)
        total_dist_3d += segment_dist
        
    if has_explicit_time:
        start_time = gpstrack[0][3]
        end_time = gpstrack[-1][3]
        total_time_seconds = abs(end_time - start_time)
    else:
        number_of_steps = len(gpstrack) - 1
        total_time_seconds = number_of_steps * 2.0

    if total_time_seconds == 0:
        return 0.0
        
    speed_mps = total_dist_3d / total_time_seconds
    
    return speed_mps * 3.6

def breakTime(gpstrack, maxdelta):
    if len(gpstrack) == 0:
        return [0]
    
    pause_list = [0]
    
    if len(gpstrack) == 1:
        return pause_list

    has_explicit_time = (len(gpstrack[0]) == 4)

    for i in range(1, len(gpstrack)):
        p1 = gpstrack[i-1]
        p2 = gpstrack[i]
        
        dx = p2[0] - p1[0]
        dy = p2[1] - p1[1]
        dz = p2[2] - p1[2]
        dist = math.sqrt(dx**2 + dy**2 + dz**2)
        
        if has_explicit_time:
            dt = abs(p2[3] - p1[3])
        else:
            dt = 2.0 
            
        if dist <= maxdelta:
            current_pause_sum = pause_list[i-1] + dt
            pause_list.append(current_pause_sum)
        else:
            pause_list.append(0)
            
    return pause_list

def numberBreaks(gpstrack, maxdelta, minseconds):

    pause_values = breakTime(gpstrack, maxdelta)
    
    count = 0
    
    for i in range(len(pause_values)):
        current_val = pause_values[i]
        
        if i == 0:
            prev_val = 0
        else:
            prev_val = pause_values[i-1]
        
        if current_val >= minseconds and prev_val < minseconds:
            count += 1
            
    return count

def smooth(gpstrack, weights=[0.33, 0.33, 0.33]):

    if len(gpstrack) < 3:
        return gpstrack[:] 


    new_track = [gpstrack[0]]

    for i in range(1, len(gpstrack) - 1):
        p_prev = gpstrack[i-1]
        p_curr = gpstrack[i]
        p_next = gpstrack[i+1]

        new_x = weights[0] * p_prev[0] + weights[1] * p_curr[0] + weights[2] * p_next[0]
        new_y = weights[0] * p_prev[1] + weights[1] * p_curr[1] + weights[2] * p_next[1]
        new_z = weights[0] * p_prev[2] + weights[1] * p_curr[2] + weights[2] * p_next[2]

        new_point = [new_x, new_y, new_z]

        if len(p_curr) > 3:
            new_point.append(p_curr[3])

        new_track.append(new_point)

    new_track.append(gpstrack[-1])

    return new_track

test_track = [ [1,1,1], [4,2,1], [10,0,2] ]
test_weights = [0.2, 0.6, 0.2]

result = smooth(test_track, test_weights)

print(f"Original: {test_track}")
print(f"Geglättet: {result}")

def speedDifference(gpstrack, weightsA=[0.0, 1.0, 0.0], weightsB=[0.33, 0.33, 0.33]):
    track_a = smooth(gpstrack, weightsA)
    
    track_b = smooth(gpstrack, weightsB)
    
    time_a = plan(track_a)
    time_b = plan(track_b)
    
    diff = abs(time_a - time_b)
    
    return diff
