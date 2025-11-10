import random
#   รับค่า grapgh
graph_data = []
distance = 1
while distance > 0:
    start = input("Start: ")
    finish = input("Finish: ")
    distance = int(input("Distance:"))
    if distance == 0:
        break
    graph_data.append({
        'start': start,
        'finish': finish,
        'distance': distance,
    })
print("Graph data:", graph_data)

# B - C : 2
# C - D : 3
# A - B : 4
#======prim algo====

def prim():
    #สุ่มเลือกราก
    root = random.choice([i['start'] for i in graph_data])
    #นนรวม
    total_weight = 0
    #เก็บจุดที่เคยผ่าน
    route = set()
    # เก็บคำตอบว่าผ่านเส้นไหนบ้าง
    path =[]
    # อยากได้ว่าสเต็ป 2 กับ 3
    for i in graph_data:
        while route['start'] != route['finish']:
            # if distance == distance:
            #     candidate = sorted(route, key=str.lower)
            #เปลี่ยนเป็น route ได้ไหมตรง lambda
            edges = sorted(graph_data, key= lambda x: x['distance'])
            total_weight += i['distance']
    print("prim",root)
    print("total weight:", total_weight)
    print("path:", path)
prim()

#======Kru algo======
def kru():
    #เรียงลำดับนน.
    root = sorted(graph_data, key=lambda k: k['distance'])
    #เพื่ออะไร
    route= set()
    #เก็บเส้นทางที่ไป
    ans=[]
    #นนรวม
    total = 0
    for i in root:
        s=i['start']
        f=i['finish']

        if s not in route or f not in route:
            ans.append(i)
            route.add(s)
            route.add(f)
    total = sum(r['distance'] for r in ans)
    print("Total weight kru =", total)
kru()

