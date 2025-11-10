import random


def prim():
    # if not graph_data:
    #     print("No graph data!")
    #     return

    prim_data = []
    total_weight = 0

    # สุ่มเลือก node เริ่มต้น
    root = random.choice([edge['start'] for edge in graph_data])
    print("\nRandom start node:", root)

    # เก็บ node ที่เยือนแล้ว
    visited = {root}

    # รวม node ทั้งหมดในกราฟ
    all_nodes = set([e['start'] for e in graph_data] + [e['finish'] for e in graph_data])

    while visited != all_nodes:
        # หาขอบที่เชื่อมจาก node ที่เยือนแล้ว ไปยัง node ที่ยังไม่ได้เยือน
        candidate_edges = [
            e for e in graph_data
            if (e['start'] in visited and e['finish'] not in visited)
               or (e['finish'] in visited and e['start'] not in visited)
        ]

        if not candidate_edges:
            break

        # เลือกเส้นที่มีน้ำหนักน้อยที่สุด
        min_edge = min(candidate_edges, key=lambda e: e['distance'])

        prim_data.append(min_edge)
        total_weight += min_edge['distance']

        # เพิ่ม node ใหม่เข้าสู่ชุดที่เยือนแล้ว
        visited.add(min_edge['start'])
        visited.add(min_edge['finish'])

    print("\nPrim's Minimum Spanning Tree:")
    for edge in prim_data:
        print(f"{edge['start']} - {edge['finish']} : {edge['distance']}")

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
