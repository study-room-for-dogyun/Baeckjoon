def move_disk(disk_num, start_peg, end_peg):
    print("%d번 원판을 %d번 기둥에서 %d번 기둥으로 이동" % (disk_num, start_peg, end_peg))

def hanoi(num_disks, start_peg, end_peg):
    if num_disks == 0:
        return
    
    other_peg = 6 - start_peg - end_peg
    hanoi(num_disks - 1, start_peg, other_peg)    # 일단 작은 원판을 가운데로 옮긴다음
    move_disk(num_disks, start_peg, end_peg)        # 그다음 크기 원판을 마지막으로 옮기고
    hanoi(num_disks - 1, other_peg, end_peg)      # 다시 작은 원판을 가운데서 마지막으로 옮김
    
hanoi(3, 1, 3)