ub, i, l):
        return sub[:i] + sub[i:i+l][::-1] + sub[i+l:]

    def query(sub, i, l):
            if '1' not in sub[i:i+l]:
                        return 0
                        num = 1
                            while '1'*num in sub[i:i+l]:
                                        num += 1
                                            return num-1

                                        go = input().split(' ')[1]
                                        sub = input()
                                        for row in range(int(go)):
                                                t, i, l = input().split(' ')
                                                    t, i, l = int(t), int(i), int(l)
                                                        if t == 1:
                                                                    sub = update(sub, i, l)
                                                                        else:
                                                                                    fin = query(sub, i, l)
                                                                                            print(fin)
                                                                                             ') ')
