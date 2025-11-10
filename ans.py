import random

def prim():
    # ---- เตรียมข้อมูล ----
    total_weight = 0
    mst = []  # เก็บเส้นทางที่เลือก
    nodes = set()  # เก็บ node ทั้งหมด

    # รวม node ทั้งหมดจากกราฟ
    for e in graph_data:
        nodes.add(e['start'])
        nodes.add(e['finish'])

    # เลือก node เริ่มต้นแบบสุ่ม
    root = random.choice(list(nodes))
    visited = {root}
    print("เริ่มจาก:", root)

    # ---- เริ่มสร้างต้นไม้ MST ----
    while visited != nodes:
        candidate_edges = []

        # หาขอบที่เชื่อมจาก node ที่เยือนแล้ว ไปยัง node ที่ยังไม่เยือน
        for e in graph_data:
            if (e['start'] in visited and e['finish'] not in visited) or \
               (e['finish'] in visited and e['start'] not in visited):
                candidate_edges.append(e)

        # ถ้าไม่มีเส้นที่ต่อได้ -> จบ (กราฟไม่เชื่อมถึงกัน)
        if not candidate_edges:
            break

        # เลือกเส้นที่น้ำหนักน้อยที่สุด
        min_edge = min(candidate_edges, key=lambda x: x['distance'])

        # เพิ่มลงใน MST
        mst.append(min_edge)
        total_weight += min_edge['distance']

        # เพิ่ม node ใหม่เข้า visited
        visited.add(min_edge['start'])
        visited.add(min_edge['finish'])
    for e in mst:
        print(f"{e['start']} - {e['finish']} : {e['distance']}")
    print("Total Weight =", total_weight)

def kru():
    # เรียง edge จากน้อยไปมากตามน้ำหนัก
    edges = sorted(graph_data, key=lambda x: x['distance'])

    route = []  # เก็บเส้นที่เลือกเข้า MST
    nodes = set()  # เก็บจุด (node) ที่ถูกเชื่อมแล้ว

    for e in edges:
        s = e['start']
        f = e['finish']

        # ถ้ายังไม่มี node ไหนใน route หรือยังไม่เชื่อมครบทุก node
        if s not in nodes or f not in nodes:
            route.append(e)
            nodes.add(s)
            nodes.add(f)

    # แสดงผล
    print("Kruskal (ฉบับง่าย):")
    for r in route:
        print(f"{r['start']} - {r['finish']} : {r['distance']}")
    total = sum(r['distance'] for r in route)
    print("Total weight =", total)
