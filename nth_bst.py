#!/bin/python3

import sys
import math
from graphviz import Digraph


def maximise(parts):
    orig_levels = math.ceil(math.log2(len(parts) + 1))
    level = 0
    # print(parts)
    while level < orig_levels:
        valid_a = 2 ** (level) - 1
        valid_b = 2 ** (level + 1) - 1
        # print("level {} valid_a {} valid_b {}".format(level, valid_a, valid_b))
        for idx in range(valid_a, valid_b):
            d = parts[idx].strip()
            # print("Maximising idx {} ({})".format(idx, d))
            if d == "null":
                ins_pos = 2 * idx + 1
                parts.insert(ins_pos, "null")
                parts.insert(ins_pos + 1, "null")
                # print("null found at idx {} insert to {}".format(idx, ins_pos))
                # print(parts)
        level += 1
    return parts


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 nth_bst.py input_bst_data root_value")
        sys.exit(1)

    input_file = sys.argv[1]
    root_value = int(sys.argv[2])
    with open(input_file, "r") as f:
        text = ""
        for line in f.readlines():
            text += line.strip("][\n")

        parts = text.split(",")
        parts = [x.strip() for x in parts]

        parts = maximise(parts)

        levels = math.ceil(math.log2(len(parts) + 1) - 1)
        print("There are {} levels".format(levels))

        found_at = parts.index(str(root_value))

        level_found = math.floor(math.log2(found_at + 1))

        print(
            "Value {} found at pos {} at level {}".format(
                root_value, found_at, level_found
            )
        )

        left_margin = 3
        right_margin = 3
        levels_down = 3
        levels_up = 1

        start_level = max(0, level_found - levels_up)
        print(
            "Start at {} level, margins: {}, {}, {} levels down".format(
                start_level, left_margin, right_margin, levels_down
            )
        )
        for idx in range(levels_up):
            found_at = (found_at - 1) // 2

        dot = Digraph()

        vv = []
        valid_a = 2 ** (start_level) - 1
        valid_b = 2 ** (start_level + 1) - 1

        init_a = max(valid_a, found_at - left_margin)
        init_b = min(valid_b, 1 + right_margin + found_at)

        print(
            "init_a {} init_b {}, range {} - {}".format(
                init_a, init_b, valid_a, valid_b
            )
        )

        for i in range(init_a, init_b):
            v1 = 2 * i + 1
            v2 = 2 * i + 2
            s_i = parts[i].strip("][\n")
            s_v1 = parts[v1].strip("][\n")
            s_v2 = parts[v2].strip("][\n")
            print(
                "i = {}({}) connect with {}({}) and {}({})".format(
                    i, s_i, v1, s_v1, v2, s_v2
                )
            )
            if s_i != "null":
                dot.node(str(i), s_i)
                vv.append(v1)
                dot.node(str(v1), s_v1)
                dot.edge(str(i), str(v1))
                vv.append(v2)
                dot.node(str(v2), s_v2)
                dot.edge(str(i), str(v2))

        vv1 = []
        for i in range(0, levels_down):
            print("Level +{} vv size {}".format(i, len(vv)))
            for v in vv:
                v1 = 2 * v + 1
                v2 = 2 * v + 2
                if v1 > len(parts) or v2 > len(parts):
                    break
                s_i = parts[v].strip("][\n")
                s_v1 = parts[v1].strip("][\n")
                s_v2 = parts[v2].strip("][\n")
                print(
                    "i = {}({}) connect with {}({}) and {}({})".format(
                        v, s_i, v1, s_v1, v2, s_v2
                    )
                )
                if s_i != "null":
                    vv1.append(v1)
                    dot.node(str(v1), s_v1)
                    dot.edge(str(v), str(v1))
                    vv1.append(v2)
                    dot.node(str(v2), s_v2)
                    dot.edge(str(v), str(v2))
            vv[:] = vv1[:]
            vv1.clear()

        # print(r)
        dot.render("bst", format="png", view=True)
