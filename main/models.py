from django.db import models

# Main Category (e.g., Baseball, Basketball)
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# Links for Each Category (e.g., Player Stats, Team Info)
class CategoryLink(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="links")
    name = models.CharField(max_length=100)  # Link Name (e.g., "Top Players")
    content = models.TextField()  # Content displayed when the link is clicked

    def __str__(self):
        return f"{self.category.name} - {self.name}"


# Example for adding images or other media (if needed)
class Image(models.Model):
    link = models.ForeignKey(CategoryLink, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to='uploads/')
    description = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"Image for {self.link.name} - {self.description}"
