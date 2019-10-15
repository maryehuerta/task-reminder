set theLines to paragraphs of (read POSIX file "/Users/maryhuerta/PycharmProjects/PyRemind/todo_list.txt")
repeat with eachLine in theLines
	tell application "Reminders"
		set mylist to list "New"
		tell mylist
			make new reminder at end with properties {name:eachLine}
		end tell
	end tell
end repeat
