from django.test import TestCase
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from user_profile.forms import ProfileForm
from user_profile.models import Profile


class TestProfileForm(TestCase):
    """
    Unit tests for the ProfileForm to ensure it behaves
    correctly with valid and invalid data.
    """

    def setUp(self):
        """
        Create a test user and a fake image file for use in form tests.
        """
        self.user = User.objects.create_user(
            username="testuser", password="password")
        self.image = SimpleUploadedFile(
            name="test_image.jpg",
            content=b"fake image content",
            content_type="image/jpeg",
        )

    def test_profile_form_is_valid(self):
        """
        Test that the form is valid
        when all required fields are provided correctly.
        """
        form_data = {
            "name": "Test User",
            "about": "This is a test user.",
        }
        form = ProfileForm(data=form_data, files={"image": self.image})
        self.assertTrue(
            form.is_valid(), msg="ProfileForm should be valid with all fields."
        )

    def test_profile_form_is_invalid_without_name(self):
        """
        Test that the form is invalid when the name field is missing.
        """
        form_data = {
            "name": "",
            "about": "Some text about user.",
        }
        form = ProfileForm(data=form_data, files={"image": self.image})
        self.assertFalse(
            form.is_valid(), msg="ProfileForm should be invalid without name."
        )

    def test_profile_form_valid_without_about(self):
        """
        Test that the form is valid even when the about field is empty,
        since it is optional (blank=True in the model).
        """
        form_data = {
            "name": "Test User",
            "about": "",
        }
        form = ProfileForm(data=form_data, files={"image": self.image})
        self.assertTrue(
            form.is_valid(),
            msg="ProfileForm should be valid without about field."
        )
