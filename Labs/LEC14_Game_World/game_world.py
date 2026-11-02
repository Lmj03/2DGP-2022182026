# world = [] => 1차원 리스트
world = [ [], [] ] # 2차원 리스트로 변경 0, 1번 레이어로 나누어 관리

# 게임 월드에 객체를 추가할 때 layer를 지정해야함.
def add_object(o, layer=0): # 기본값 0
    world[layer].append(o)

# world 안에는 기본적으로 객체를 담는 '리스트'들이 있음. 
# 따라서 제거할려면 리스트 안에서 제거해야함.
def remove_object(o):
    for layer in world:
        if o in layer:
            layer.remove(o)
            return # 더 이상 찾을 필요 없음. 이미 제거했으므로

# game logic
def update():
    for layer in world:
        for o in layer:
            o.update()

# game rendering
def render():
    for layer in world:
        for o in layer:
            o.draw()
