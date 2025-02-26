package queue

type Queue struct {
	items []*any
}

func (q *Queue) enqueu(item any) {
	q.items = append(q.items, &item)

}

func (q *Queue) dequeu() any {

	if len(q.items) == 0 {
		return nil
	}

	first := q.items[0]

	q.items = q.items[1:]

	// basically first is a pointer so we have to dereference it
	return *first

}
