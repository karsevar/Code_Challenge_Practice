import "fmt"

func canFinish(numCourses int, prerequisites [][]int) bool {
	courseMap := map[int][]int{}

	for i := 0; i < numCourses; i++ {
		courseMap[i] = []int{}
	}

	for _, courses := range prerequisites {
		courseMap[courses[1]] = append(courseMap[courses[1]], courses[0])
	}

	visiting := map[int]bool{}
	visited := map[int]bool{}

	var dfs func(int) bool

	dfs = func(course int) bool {
		if _, exists := visiting[course]; exists {
			return false
		}

		if _, exists := visited[course]; exists {
			return true
		}

		visiting[course] = true

		for _, neighbor := range courseMap[course] {
			if dfs(neighbor) == false {
				return false
			}
		}

		delete(visiting, course)
		visited[course] = true

		return true
	}

	for i := 0; i < numCourses; i++ {
		if dfs(i) == false {
			return false
		}
	}

	return true
}