def common_divisors(nums):

	if len(nums) == 0:
		return []

	res = set()
	for i in range(2, round(nums[0]**0.5) + 1):
		if nums[0] % i == 0:
			res.add(i)

	for num in nums[1:]:
		temp = set()
		for j in res:
			if num % j != 0:
				temp.add(j)
		if len(res) - len(temp) == 0:
			return []
		for j in temp:
			res.remove(j)

	return list(res)


if __name__ == "__main__":
	print(*common_divisors([42, 12, 18]))
		