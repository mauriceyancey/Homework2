# No need to process files and manipulate strings - we will
# pass in lists (of equal length) that correspond to
# sites views. The first list is the site visited, the second is
# the user who visited the site.

# See the test cases for more details.
# import itertools
import re
from itertools import chain

# site_list = ["a.com", "b.com", "a.com", "b.com", "a.com", "c.com"]
# user_list = ["andy", "andy", "bob", "bob", "charlie", "charlie"]
# time_list = [1238972321, 1238972456, 1238972618, 1238972899, 1248472489, 1258861829]
# a = "a"
# b = "b"
# c = "c"
# d = "d"
# e = "e"
# f = "f"
# g = "g"
# h = "h"
#
# A = "A"
# B = "B"
# C = "C"
# D = "D"
# E = "E"
# F = "F"
# G = "G"
# H = "H"
#
#
# site_list = [a,a,b,c,c,c,d,d,e,e,f,f,g]
# user_list = [B,D,C,A,B,C,B,C,C,D,A,B,A]
# time_list = range(0,16)

def highest_affinity_old(site_list, user_list, time_list):
  # Returned string pair should be ordered by dictionary order
  # I.e., if the highest affinity pair is "foo" and "bar"
  # return ("bar", "foo").
  user_dict = {}
  user_set= set(user_list)
  permutation1 = 0
  permutation2 = 0
  permutation3 = 0
  affinity_list = [permutation1, permutation2, permutation3]
  iteration = 0
  count = [0] * len(user_set)

  for i in user_list:
    x = user_list.index(i)
    if i in user_dict:
        user_dict[i] = site_list[x], site_list[x-1]
        # user_dict.setdefault(i, {})[site_list[x]] = 1
    else:
        user_dict[i] = site_list[x]

  
  # Trying stuff out
  # for user in user_set:
  #   for key in user_dict:
  #       y = user_list.index(user)
  #       if user_dict[key] == site_list[y]:
  #          count[y] += 1
  #       else:
  #           count[y] += 1
  # print(count)

      # print(others)
  while iteration < len(user_list):
    if iteration == 0:
        if user_dict[user_list[iteration]] == user_dict[user_list[iteration+1]]:
            permutation1 += 1
    elif iteration == 1:
        if user_dict[user_list[iteration]] == user_dict[user_list[iteration+1]]:
          permutation2 +=1
    else:
        if user_dict[user_list[iteration]] == user_dict[user_list[0]]:
          permutation3 +=1
    iteration += 1

  # print(permutation1,'', permutation2,'', permutation3)

  if max(affinity_list) == permutation1:
    print(user_dict[user_list[1]])
    return user_dict[user_list[1]]
  elif max(affinity_list) == permutation2:
    print(user_dict[user_list[2]])
    return user_dict[user_list[2]]
  else:
    print(user_dict[user_list[0]])
    return user_dict[user_list[0]]

  # print(user_dict)
  # print(user_dict[user_list[1]])


# def append_value(dict_var, list_var):
def append_value(dict_key, site_var, dict_var1, dict_var2=0, dict_var3=0, dict_var4=0):
  list_tmp = []
  dict_var_tmp = (dict_var1, dict_var2, dict_var3, dict_var4)
  if 0 in dict_var_tmp:
    dict_var_tmp = [x for x in dict_var_tmp if x != 0 ]
    # dict_var_tmp = re.sub(r'([])+', '', dict_var_tmp)

    # dict_var_tmp = list(set(dict_var_tmp))
  if dict_var_tmp:
    # dict_var_tmp = dict_var_tmp.decode('unicode_escape').encode('ascii', 'ignore')
    # stripped_vars = []
    # stripped_test = []
    # val = [i.decode('UTF-8') if isinstance(i, baseString) else i for i in dict_var_tmp]
    stripped_test = list(chain.from_iterable(dict_var_tmp))
    # stripped_test.append(item for item in dict_var_tmp)
    # print((stripped_test))
    # for val in dict_var_tmp:
      # stripped_test.append(val)
      # val = str(val).strip("[]")
      # val = str(val).strip('"')
      # val = str(val).strip('\\')
      # val = str(val).strip("\\'")
      # val = str(val).strip("\\'")
      # val = val.replace("\\", "")
      # val = [orig.decode('UTF-8') if isinstance(orig, val) else orig for orig in val]
      # val.encode(utf-8)decode("utf-8", "strict")
      # stripped_vars.append(val)
    # dict_var_tmp = stripped_vars
    dict_var_tmp = stripped_test
  # dict_var_tmp.remove(0)
  # dict_var_tmp.remove(0)
  # dict_var_tmp = dict_var_tmp
  dict_length = len(dict_var_tmp)
  # for p in dict_var.values():
  #   list_tmp.append(**p)
  # for i in range(dict_length):
  dict_var_tmp.append(site_var)
  # #
  # list_tmp.append(list_var)

  for key in dict_key.keys():
     k = key
    # v = value
  #   for idx in range(dict_length):
  #     list_tmp.append(site_var)

  # k = str(k)
  # k = k[11:-2]
  # print(k)
  # print(list_tmp)
  # print(dict_var_tmp)
  # k = k[:-2]
  # print(k)
  # k = k[2:]
  # print(k)
  # dict_key[k] = list_tmp
  dict_key[k] = dict_var_tmp
  return dict_key
  # print
  # k
  # ud[k] = l
  #
  # print
  # ud

def get_count(site_val, user_dict, nums):
  counter = 0
  counts = []
  for idx, site in enumerate(site_val):
    if site in user_dict:
      counter = nums[idx] + 1
      counts.append(counter)
    else:
      counts.append(nums[idx])
  return counts

def highest_affinity(site_list, user_list, time_list):
    # Returned string pair should be ordered by dictionary order
    # I.e., if the highest affinity pair is "foo" and "bar"
    # return ("bar", "foo").
    user_sort = sorted(list(set(user_list)))
    site_sort = sorted(list(set(site_list)))
    site_counts = (0,0,0,0,0,0,0,0)
    list_length = len(user_list)
    user_dict1 = {user_sort[0] : 0}
    user_dict2 = {user_sort[1] : 0}
    user_dict3 = {user_sort[2] : 0}
    user_dict4 = {}
    user_dict5 = {}
    user_dict6 = {}
    user_dict7 = {}
    user_dict8 = {}
    user1_sites = []
    user2_sites = []
    user3_sites = []
    user4_sites = []
    user5_sites = []
    user6_sites = []
    user7_sites = []
    user8_sites = []

    if len(user_sort) >= 4:
      user_dict4 = {user_sort[3] : 0}
      if len(user_sort) >= 5:
        user_dict5 = {user_sort[4] : 0}
        user_dict6 = {user_sort[5] : 0}
        if len(user_sort) > 7:
          user_dict7 = {user_sort[6] : 0}
          user_dict8 = {user_sort[7] : 0}

    for i in range(list_length):
      if user_list[i] in user_dict1:
        user_dict_vals = user_dict1.values()
        # print(user_dict1.values())
        # print(*user_dict1)
        # print(user_dict1[user_list[i]])
        user_dict1 = append_value(user_dict1, site_list[i], user_dict1[user_list[i]])
        user1_sites = next(iter(user_dict1.values()))

      elif user_list[i] in user_dict2:
        user_dict_vals = user_dict2.values()
        # print(user_dict1.values())
        # print(*user_dict1)
        # print(user_dict1[user_list[i]])
        user_dict2 = append_value(user_dict2, site_list[i], user_dict2[user_list[i]])
        user2_sites = next(iter(user_dict2.values()))
        # get_count(site_set, user_dict2)
      elif user_list[i] in user_dict3:
        user_dict_vals = user_dict3.values()
        # print(user_dict1.values())
        # print(*user_dict1)
        # print(user_dict1[user_list[i]])
        user_dict3 = append_value(user_dict3, site_list[i], user_dict3[user_list[i]])
        user3_sites = next(iter(user_dict3.values()))
      elif len(user_sort) >= 4:
        if user_list[i] in user_dict4:
          user_dict_vals = user_dict4.values()
          user_dict4 = append_value(user_dict4, site_list[i], user_dict4[user_list[i]])
          user4_sites = next(iter(user_dict4.values()))
          # if len(user_sort) > 5:
        if user_list[i] in user_dict5:
          user_dict_vals = user_dict5.values()
          user_dict5 = append_value(user_dict5, site_list[i], user_dict5[user_list[i]])
          user5_sites = next(iter(user_dict5.values()))
        elif user_list[i] in user_dict6:
          user_dict_vals = user_dict6.values()
          user_dict6 = append_value(user_dict6, site_list[i], user_dict6[user_list[i]])
          user3_sites = next(iter(user_dict3.values()))
            # if len(user_sort) > 7:
        if user_list[i] in user_dict7:
          user_dict_vals = user_dict7.values()
          user_dict7 = append_value(user_dict7, site_list[i], user_dict7[user_list[i]])
          user7_sites = next(iter(user_dict7.values()))
        elif user_list[i] in user_dict8:
          user_dict_vals = user_dict8.values()
          user_dict8 = append_value(user_dict8, site_list[i], user_dict8[user_list[i]])
          user8_sites = next(iter(user_dict8.values()))

    user1_sites = next(iter(user_dict1.values()))
    user2_sites = next(iter(user_dict2.values()))
    user3_sites = next(iter(user_dict3.values()))
    site_counts = get_count(site_sort, user1_sites, site_counts)
    site_counts = get_count(site_sort, user2_sites, site_counts)
    site_counts = get_count(site_sort, user3_sites, site_counts)
    if len(user_sort) >= 4:
      user4_sites = next(iter(user_dict4.values()))
      site_counts = get_count(site_sort, user4_sites, site_counts)
      if len(user_sort) > 5:
        user5_sites = next(iter(user_dict5.values()))
        user6_sites = next(iter(user_dict6.values()))
        site_counts = get_count(site_sort, user5_sites, site_counts)
        site_counts = get_count(site_sort, user6_sites, site_counts)
        if len(user_sort) > 7:
          user7_sites = next(iter(user_dict7.values()))
          user8_sites = next(iter(user_dict8.values()))
          site_counts = get_count(site_sort, user7_sites, site_counts)
          site_counts = get_count(site_sort, user8_sites, site_counts)

    top_counts_list = sorted(site_counts, key=int, reverse=True)
    one = top_counts_list[0]
    two = top_counts_list[1]
    top_site = 'None'
    second_site = 'None'
    for idx, c in enumerate(site_counts):
      if c == one:
        if top_site != 'None':
          second_site = site_sort[idx]
          continue
        top_site = site_sort[idx]
      elif c == two:
        second_site = site_sort[idx]
    affinity_list = (top_site, second_site)
    # answer_list =
    # answer_list.append(sorted(affinity_list))
    answer_list = sorted(affinity_list)
    return answer_list[0], answer_list[1]
    # top_count = max(site_counts)
    # x = 0
    # y = 0
    # while x <= top_count and y != site_sort[top_count]:
    #   second_site =
    # second_count = max(site_counts.pop(str(top_count)))
    # top_site = site_sort[top_count]
    # second_site = site_sort[second_count]
    # print("top site is " +top_site)
    # print("second site is " +second_site)
    # print(user1_sites)
    # print(user2_sites)
    # print(user3_sites)
    # if site_list[5] in user1_sites:
      # print(type(user1_sites))

    # for i in user_list:
    #   x = user_list.index(i)
    #   if i in user_dict:
    #     user_dict[i] = site_list[x], site_list[x - 1]
    #     # user_dict.setdefault(i, {})[site_list[x]] = 1
    #   else:
    #     user_dict[i] = site_list[x]


        # Trying stuff out
        # for user in user_set:
        #   for key in user_dict:
        #       y = user_list.index(user)
        #       if user_dict[key] == site_list[y]:
        #          count[y] += 1
        #       else:
        #           count[y] += 1
        # print(count)

        # print(others)
    # while iteration < len(user_list):
    #   if iteration == 0:
    #     if user_dict[user_list[iteration]] == user_dict[user_list[iteration + 1]]:
    #       permutation1 += 1
    #   elif iteration == 1:
    #     if user_dict[user_list[iteration]] == user_dict[user_list[iteration + 1]]:
    #       permutation2 += 1
    #   else:
    #     if user_dict[user_list[iteration]] == user_dict[user_list[0]]:
    #       permutation3 += 1
    #   iteration += 1

    # print(permutation1,'', permutation2,'', permutation3)

    # if max(affinity_list) == permutation1:
    #   print(user_dict[user_list[1]])
    #   return user_dict[user_list[1]]
    # elif max(affinity_list) == permutation2:
    #   print(user_dict[user_list[2]])
    #   return user_dict[user_list[2]]
    # else:
    #   print(user_dict[user_list[0]])
    #   return user_dict[user_list[0]]


# highest_affinity(site_list, user_list, time_list)
#

