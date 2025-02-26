package queue

import "container/heap"

type EmergencyRoom struct {
	patientsQueue PatientsQueue
}

func NewEmergencyRoom() *EmergencyRoom {

	// create a new PatientsQueue and initialise it with 0 size
	er := &EmergencyRoom{patientsQueue: make(PatientsQueue, 0)}

	heap.Init(er)

	return er
}
