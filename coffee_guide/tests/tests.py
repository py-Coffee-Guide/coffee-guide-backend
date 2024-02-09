# from django.test import TestCase
# from django.urls import reverse
# from rest_framework.test import APIClient
# from rest_framework import status

# from api.serializers.cafe import CafeGetSerializer
# from cafe.models import Cafe


# class CafeGetSerializerTestCase(TestCase):
#     def setUp(self):
#         self.client = APIClient()
#         self.cafe_data = {
#             'name': 'Test Cafe',
#             'description': 'Test description',
#             # Add other required fields
#             # ...
#         }
#         self.serializer = CafeGetSerializer(data=self.cafe_data)

#     def test_valid_data(self):
#         self.assertTrue(self.serializer.is_valid())

#     def test_invalid_data(self):
#         invalid_data = {
#             'name': '',
#             'description': 'Test description',
#             # Add other required fields
#             # ...
#         }
#         serializer = CafeGetSerializer(data=invalid_data)
#         self.assertFalse(serializer.is_valid())

#     def test_create_cafe(self):
#         response = self.client.post(reverse('cafe-list'), self.cafe_data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         self.assertEqual(Cafe.objects.count(), 1)
#         self.assertEqual(Cafe.objects.get().name, 'Test Cafe')


# import time
# from django.test import TestCase
# from django.urls import reverse
# from rest_framework.test import APIClient

# class APITimingTestCase(TestCase):
#     def setUp(self):
#         self.client = APIClient()
#         # Ensure you have some initial data if needed
        
#     def test_request_time(self):
#         start_time = time.time()
#         response = self.client.get(reverse('api:cafes-list'))
#         end_time = time.time()
        
#         # Ensure the request was successful
#         self.assertEqual(response.status_code, 200)
        
#         # Calculate and print the request time
#         request_time = end_time - start_time
#         print(f"Request took {request_time} seconds to complete.")
        
#         # Assert that the request time is within an acceptable range
#         # Example: Assert that the request time is less than 1 second
#         self.assertTrue(request_time < 1.0, "Request time is too high!")