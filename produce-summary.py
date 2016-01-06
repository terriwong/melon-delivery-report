day = 1
date = 20140519

while day <= 3:
    print "Day %d" % day
    file_name = "um-deliveries-" + str(date) + ".txt"
    the_file = open(file_name)
    for line in the_file:
        line = line.rstrip()
        words = line.split('|')

        melon = words[0]
        count = words[1]
        amount = words[2]

        print "Delivered {} {}s for total of ${}".format(count, melon, amount)
    the_file.close()

    day += 1
    date += 1



# print "Day 1"
# the_file = open("um-deliveries-20140519.txt")
# for line in the_file:
#     line = line.rstrip()
#     words = line.split('|')

#     melon = words[0]
#     count = words[1]
#     amount = words[2]

#     print "Delivered {} {}s for total of ${}".format(
#         count, melon, amount)
# the_file.close()


# print "Day 2"
# the_file = open("um-deliveries-20140520.txt")
# for line in the_file:
#     line = line.rstrip()
#     words = line.split('|')

#     melon = words[0]
#     count = words[1]
#     amount = words[2]

#     print "Delivered {} {}s for total of ${}".format(
#         count, melon, amount)
# the_file.close()


# print "Day 3"
# the_file = open("um-deliveries-20140521.txt")
# for line in the_file:
#     line = line.rstrip()
#     words = line.split('|')

#     melon = words[0]
#     count = words[1]
#     amount = words[2]

#     print "Delivered {} {}s for total of ${}".format(
#         count, melon, amount)
# the_file.close()
