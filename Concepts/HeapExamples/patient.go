package queue

type SeviorityStatus int

const (
	Mild SeviorityStatus = iota
	Moderate
	Critical
)

type Patient struct {
	name       string
	serviority SeviorityStatus
}
