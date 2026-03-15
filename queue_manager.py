
from collections import deque

patient_queue = deque()
patients_seen_today = []

def add_patient(patient):
    patient_queue.append(patient)

def next_patient():
    if len(patient_queue) > 0:
        patient = patient_queue.popleft()
        patients_seen_today.append(patient)
        return patient
    return None

def get_queue():
    return list(patient_queue)

def total_seen():
    return len(patients_seen_today)
