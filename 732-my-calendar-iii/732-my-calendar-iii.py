class MyCalendarThree:

    def __init__(self):
        self.starts = []
        self.ends = []
        self.bookings = {}
        self.k = 1
        
    def book(self, start: int, end: int) -> int:
		# Handle the first call so the console stops throwing Index Error
        if not self.starts:
            self.starts = [start]
            self.ends = [end]
            self.bookings[start] = 1
            return 1
        
		# The index of the earliest start time at or after the new one (and where start will ultimately be inserted)
        i = bisect_left(self.starts, start)
            
		# Earlier than any prior start time
        if i == 0 and self.starts[i] > start:
            self.bookings[start] = 1
        
		# The start time is unique up to this point AND there's at least one booking started before
		# We need to calculate how many bookings are going on when this one starts
        elif i == len(self.starts) or self.starts[i] != start:
		
			# The start time of the last booking and k at that point
            prev = self.starts[i-1]
            base = self.bookings[prev]
			
			# Now we need to count down how many bookings will end between then and the new booking starting
            end_i = bisect_right(self.ends, prev)
            while base > 0 and self.ends[end_i] <= start:
                base -= 1
                end_i += 1
				
			# At the start of the new booking, there will be that booking plus any previous still going on (base)
            self.bookings[start] = base + 1
            self.k = max(self.k, base + 1)

		# For every unique start time in the interval [start, end), increment it in bookings
        j = i
        while j < len(self.starts) and self.starts[j] < end:
                self.bookings[self.starts[j]] += 1
                self.k = max(self.k, self.bookings[self.starts[j]])
                j += 1
				# Keys in bookings are unique, but elements in starts are not
                while j < len(self.starts) and self.starts[j] == self.starts[j-1]:
                    j += 1
            
		# Update our start and end arrays, using i from before to spare a binary search
        self.starts.insert(i, start)
        insort(self.ends, end)
        
        return self.k