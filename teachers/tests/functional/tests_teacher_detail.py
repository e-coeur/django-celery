from elk.utils.testing import ClientTestCase, create_customer, create_teacher
from teachers.slot_list import SlotList


class TestTeacherDetail(ClientTestCase):
    def setUp(self):
        self.teacher = create_teacher(works_24x7=True)

    def test_loading(self):
        response = self.c.get('/teachers/%s/' % self.teacher.user.username)

        with self.assertHTML(response, 'img.teacher-face') as teacher_face:
            self.assertIsNotNone(teacher_face)

    def test_no_teacher_detail_for_non_teacher_user(self):
        some_random_man = create_customer()
        response = self.c.get('/teachers/%s/' % some_random_man.user.username)

        self.assertEqual(response.status_code, 404)

    def test_teacher_detail_slots_list(self):
        response = self.c.get('/teachers/%s/' % self.teacher.user.username)
        self.assertGreaterEqual(len(response.context['timeslots']), 7)

        first_day = response.context['timeslots'][0]
        self.assertIsInstance(first_day['slots'], SlotList)
        self.assertGreaterEqual(len(first_day['slots']), 10)
