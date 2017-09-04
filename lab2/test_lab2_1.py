from hw2_set import OurSet

def test_add_empty_set():
	""" 1: Add value to empty set """
	s = OurSet()
	res = s.add(5)
	assert len(s) == 1
	assert res == True

def test_add_duplicate():
	""" 2: Add duplicate value to set """
	s = OurSet()
	res = s.add(5)

	res = s.add(5)
	assert len(s) == 1
	assert res == False

def test_add_non_duplicate():
	""" 3: Add non-duplicate value to set """
	s = OurSet()
	res = s.add(5)

	res = s.add(6)
	assert len(s) == 2
	assert res == True

def test_addList_duplicate():
	""" 4: Add list containing only duplicate values to set """
	s = OurSet()
	res = s.add(5)
	res = s.add(6)

	res = s.add_list([5, 6])
	assert len(s) == 2
	assert res == False

def test_addList_non_duplicate():
	""" 5: Add list containing some non-duplicate values to set """
	s = OurSet()
	res = s.add(5)
	res = s.add(6)

	res = s.add_list([3, 2, 5])
	assert len(s) == 4
	assert res == True

def test_len_empty_set():
	""" 6: Length of empty set """
	s = OurSet()

	assert len(s) == 0

def test_len_non_empty_set():
	""" 7: Length of non-empty set """
	s = OurSet()
	s.add(5)

	assert len(s) == 1