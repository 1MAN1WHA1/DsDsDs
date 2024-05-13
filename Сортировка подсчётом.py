def counting_sort(arr):
    max_num = max(arr)
    min_num = min(arr)
    count = [0] * (max_num - min_num + 1)
    for num in arr:
        count[num - min_num] += 1
    sorted_arr = []
    for i in range(len(count)):
        sorted_arr += [i + min_num] * count[i]
    return sorted_arr

arr = [372, 891, 504, 178, 668, 782, 616, 769, 205, 914, 273, 892, 189, 160, 450, 735, 481, 378, 995, 587, 156, 694, 980, 888, 740, 22, 440, 282, 48, 931, 203, 942, 320, 926, 545, 993, 697, 59, 438, 885, 51, 625, 762, 700, 138, 420, 22, 821, 987, 484, 295, 949, 58, 48, 486, 578, 604, 676, 312, 654, 273, 703, 509, 697, 458, 394, 901, 552, 446, 439, 368, 970, 140, 301, 178, 422, 760, 858, 31, 9, 849, 738, 467, 209, 506, 991, 524, 804, 124, 515, 611, 71, 438, 605, 77, 892, 777, 212, 57, 280, 615, 332, 344, 154, 498, 591, 84, 603, 693, 285, 734, 950, 335, 227, 576, 396, 221, 18, 569, 803, 327, 420, 764, 500, 743, 10, 522, 516, 84, 21, 556, 478, 712, 687, 510, 763, 858, 974, 802, 593, 770, 831, 604, 497, 50, 349, 22, 516, 897, 739, 517, 459, 463, 927, 126, 202, 695, 514, 161, 674, 114, 828, 272, 810, 875, 82, 951, 283, 543, 647, 792, 596, 444, 922, 51, 452, 77, 673, 647, 539, 314, 676, 275, 953, 44, 233, 374, 606, 672, 972, 383, 92, 31, 805, 496, 593, 795, 334, 8, 402, 125, 472, 7, 631, 315, 89, 906, 345, 961, 73, 699, 71, 978, 17, 401, 108, 462, 451, 505, 462, 597, 678, 393, 784, 664, 625, 820, 725, 362, 222, 908, 45, 76, 660, 740, 43, 216, 497, 180, 531, 877, 293, 139, 625, 533, 662, 252, 17, 620, 516, 176, 945, 234, 794, 49, 634, 43, 545, 927, 868, 294, 197, 561, 574, 221, 788, 582, 554, 867, 989, 471, 728, 512, 787, 905, 47, 917, 199, 798, 748, 125, 302, 473, 383, 977, 171, 532, 717, 578, 906, 779, 83, 465, 540, 11, 569, 294, 946, 837, 152, 575, 873, 98, 160, 878, 510, 965, 328, 49, 62, 945, 756, 884, 84, 473, 164, 605, 716, 973, 102, 454, 179, 163, 374, 134, 15, 193, 655, 632, 962, 678, 855, 615, 866, 130, 783, 370, 35, 826, 695, 150, 313, 553, 138, 495, 453, 978, 93, 277, 374, 508, 822, 960, 251, 615, 112, 364, 113, 988, 145, 67, 603, 715, 871, 502, 686, 697, 190, 119, 897, 575, 801, 70, 104, 949, 570, 131, 390, 801, 999, 846, 131, 779, 327, 50, 949, 225, 77, 8, 363, 188, 62, 643, 663, 253, 61, 140, 343, 850, 78, 486, 68, 704, 51, 142, 564, 755, 256, 71, 145, 47, 932, 608, 182, 405, 884, 46, 115, 72, 367, 904, 886, 651, 654, 204, 220, 203, 189, 215, 693, 71, 567, 239, 848, 212, 484, 934, 441, 876, 873, 808, 766, 961, 212, 724, 693, 400, 238, 437, 41, 616, 618, 562, 978, 630, 317, 842, 535, 306, 249, 475, 36, 245, 16, 888, 792, 66, 39, 800, 903, 381, 654, 500, 530, 435, 97, 442, 122, 200, 324, 971, 848, 915, 670, 229, 648, 612, 374, 767, 458, 84, 764, 368, 637, 375, 474, 138, 105, 663, 506, 244, 482, 8, 244, 449, 180, 498, 308, 849, 865, 963, 53, 880, 788, 121, 744, 294, 667, 49, 899, 117, 208, 277, 504, 802, 643, 799, 593, 370, 869, 734, 307, 525, 769, 892, 803, 93, 415, 24, 741, 802, 943, 925, 439, 486, 827, 636, 949, 876, 390, 540, 190, 834, 405, 455, 801, 296, 242, 180, 738, 940, 91, 138, 915, 465, 155, 129, 159, 113, 597, 146, 779, 657, 825, 25, 538, 927, 547, 936, 640, 465, 659, 724, 743, 220, 844, 545, 171, 298, 530, 68, 821, 7, 614, 320, 690, 481, 204, 279, 565, 771, 183, 768, 51, 539, 708, 791, 361, 758, 912, 950, 469, 571, 870, 689, 951, 447, 677, 118, 318, 747, 759, 129, 794, 497, 791, 835, 578, 936, 424, 799, 309, 190, 124, 661, 295, 122, 676, 429, 986, 594, 224, 905, 689, 682, 713, 628, 262, 635, 824, 283, 946, 214, 234, 876, 719, 115, 127, 226, 858, 161, 859, 35, 47, 702, 965, 191, 873, 495, 787, 977, 177, 642, 594, 172, 64, 98, 785, 415, 37, 263, 53, 162, 78, 107, 537, 720, 706, 375, 908, 423, 282, 964, 442, 429, 60, 739, 754, 826, 286, 263, 285, 435, 768, 727, 926, 867, 372, 324, 126, 732, 760, 491, 640, 709, 983, 993, 782, 370, 855, 530, 216, 327, 477, 514, 36, 767, 57, 164, 692, 209, 207, 363, 547, 265, 859, 318, 110, 875, 837, 665, 773, 186, 335, 274, 931, 675, 299, 258, 231, 771, 861, 161, 112, 383, 366, 158, 875, 882, 174, 138, 175, 921, 861, 430, 63, 939, 159, 834, 166, 289, 497, 457, 48, 312, 161, 671, 216, 755, 928, 724, 308, 734, 589, 715, 535, 964, 134, 530, 243, 394, 180, 553, 296, 232, 35, 726, 407, 192, 823, 986, 280, 759, 5, 262, 308, 127, 479, 128, 699, 743, 104, 928, 486, 13, 879, 37, 501, 339, 563, 991, 472, 142, 684, 759, 84, 810, 478, 472, 961, 356, 415, 939, 299, 194, 88, 568, 642, 744, 494, 884, 389, 497, 763, 734, 17, 352, 771, 616, 777, 487, 71, 382, 195, 705, 484, 872, 874, 569, 773, 842, 753, 42, 677, 218, 924, 848, 28, 49, 291, 215, 700, 319, 473, 119, 61, 161, 11, 312, 104, 725, 496, 535, 30, 487, 340, 951, 903, 924, 537, 358, 755, 240, 184, 414, 259, 654, 651, 316, 834, 237, 82, 452, 314, 213, 211, 846, 716, 477, 330, 512, 575, 768, 291, 314, 810, 467, 972, 133, 23, 563, 762, 642, 997, 298, 980, 672, 289, 716, 961, 734, 578, 630, 153, 186, 484, 417, 99, 116, 738, 816, 666, 576, 301, 859, 280, 58, 175, 251, 688, 572, 561, 361, 878, 697, 819, 285, 741, 134, 567, 731, 960, 911, 200, 51, 803, 152, 466, 848, 868, 307, 992, 407, 507, 241, 736, 34, 271, 160, 400, 167, 840, 281, 116, 488, 94, 936, 27, 157, 707, 837, 191, 682, 800, 771, 475, 435, 879, 110, 988, 763, 539, 628, 997, 438, 961, 720, 443, 894, 809, 901, 422, 324, 500, 498, 293, 693, 94, 378, 49, 815, 164, 428, 292, 115, 478, 809, 706, 703, 756, 245, 753, 916, 549, 173, 585, 661, 309, 663, 552, 144, 916, 392, 111, 422, 293, 773, 623, 387, 939, 144, 31, 493, 763, 583, 624, 815, 868, 589, 154, 296, 194, 699, 416, 294, 749, 728, 189, 783, 304, 102, 194, 77, 574, 841, 146, 440, 654, 647, 330, 769, 878, 781, 318, 409, 336, 712, 591, 667, 673, 444, 611, 989, 497, 647, 379, 902, 730, 790, 128, 214, 55, 751, 313, 771, 212, 805, 683, 68, 914, 960, 73, 592, 126, 723, 607, 871, 826, 451, 880, 138, 646, 394, 294, 141, 230, 870, 914, 119, 843, 151, 708, 119, 489, 744, 124, 508, 589, 334, 217, 37, 860, 437, 785, 32, 821, 267, 168, 319, 751, 241, 855, 938, 127, 879, 948, 751, 649, 582, 900, 475, 679, 597, 777, 869, 929, 216, 331, 10, 137, 51, 611, 290, 15, 358, 438, 354, 475, 875, 147, 916, 623, 264, 884, 507, 525, 830, 792, 22, 473, 158, 934, 880, 335, 430, 685, 953, 607, 619, 849, 571, 750, 487, 255, 115, 146, 465, 915, 332, 733, 685, 867, 320, 81, 7, 301, 825, 515, 484, 891, 308, 306, 71, 363, 354, 804, 10, 424, 694, 279, 130]

arr = counting_sort(arr)
print("Сортировка подсчётом:", arr)
#Подсчитывает количество каждого элемента в списке и затем создаёт отсортированный список на основе этих подсчётов. Используется, когда известен диапазон возможных значений