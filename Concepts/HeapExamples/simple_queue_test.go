package queue

import "testing"

func TestQueue(t *testing.T) {

	q := &Queue{}

	q.enqueu("a")
	q.enqueu("b")

	en1 := q.dequeu()

	if en1 != "a" {
		t.Error(" supposed to get a")
	}

	en2 := q.dequeu()

	if en2 != "b" {
		t.Error(" supposed to get b")
	}

	en3 := q.dequeu()

	if en3 != nil {
		t.Error(" this is supposed to be nil")
	}

}
