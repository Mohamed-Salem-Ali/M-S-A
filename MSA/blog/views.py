from datetime import date

from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound,request
# Create your views here.


from datetime import date

all_posts = [
    {
        "slug": "intro-to-python",
        "image": "python_intro.jpg",
        "author": "John Doe",
        "date": date(2023,1,15),
        "title": "Introduction to Python",
        "excerpt": "Learn the basics of Python, a versatile programming language.",
        "content": """Python is a powerful programming language used for a wide range of applications. In this post, we cover the basics of Python programming, including variables, data types, and control structures.
                      Additionally, we discuss the importance of Python's extensive standard library and how it simplifies many programming tasks. We also provide examples of real-world applications where Python excels, such as web development, data analysis, and automation."""
    },
    {
        "slug": "deep-learning",
        "image": "deep_learning.jpg",
        "author": "Jane Smith",
        "date": date(2024,7,16),
        "title": "Understanding Deep Learning",
        "excerpt": "Explore the world of deep learning and neural networks.",
        "content": """Deep learning is a subset of machine learning that uses neural networks with many layers. This post delves into the concepts of deep learning, its applications, and how it is revolutionizing fields like computer vision and natural language processing.
                      We also cover the types of neural networks, including convolutional and recurrent networks, and their specific use cases. Furthermore, we discuss popular frameworks like TensorFlow and PyTorch that make implementing deep learning models more accessible."""
    },
    {
        "slug": "cloud-computing",
        "image": "cloud_computing.jpg",
        "author": "Alice Johnson",
        "date": date(2024,7,16),
        "title": "The Rise of Cloud Computing",
        "excerpt": "Discover how cloud computing is changing the tech landscape.",
        "content": """Cloud computing allows for on-demand availability of computing resources over the internet. This post discusses the benefits of cloud computing, its key service models (IaaS, PaaS, SaaS), and major providers like AWS, Azure, and Google Cloud.
                      We also explore the impact of cloud computing on businesses, enabling them to scale operations efficiently and cost-effectively. Security concerns and best practices for using cloud services are also addressed, along with future trends in the cloud computing landscape."""
    },
    {
        "slug": "cybersecurity-basics",
        "image": "cybersecurity.jpg",
        "author": "Bob Brown",
        "date": date(2024,7,16),
        "title": "Cybersecurity Basics",
        "excerpt": "An introduction to the fundamental concepts of cybersecurity.",
        "content": """Cybersecurity involves protecting computer systems and networks from information disclosure, theft, or damage. In this post, we cover the basics of cybersecurity, common threats, and best practices to safeguard your digital assets.
                      Additionally, we delve into different types of cyber attacks such as phishing, malware, and ransomware. Strategies for personal and organizational security, including the use of firewalls, antivirus software, and regular security audits, are also discussed in detail."""
    },
    {
        "slug": "future-of-ai",
        "image": "future_ai.jpg",
        "author": "Eve Davis",
        "date": date(2024,7,16),
        "title": "The Future of Artificial Intelligence",
        "excerpt": "A look into the future developments and implications of AI.",
        "content": """Artificial Intelligence (AI) is rapidly evolving and impacting various industries. 
        This post explores future trends in AI, potential ethical concerns, and how AI could shape the future of work, healthcare, and daily life.
        We also examine emerging AI technologies such as autonomous vehicles, AI-driven healthcare diagnostics, and smart home systems. 
        The societal implications of AI, including job displacement and privacy concerns, are considered, alongside the role of regulation in guiding ethical AI development."""
    }
]

def get_date(post):
    return post['date']

def post_detail(request,slug):
    identified_post = next(post for post in all_posts if post['slug']==slug)
    return render(request, "blog/post-detail.html",{
        "post": identified_post
    })

def starting_page(request):
    sorted_posts=sorted(all_posts,key=get_date)
    latest_posts=sorted_posts[-3:]
    return render(request,"blog/home.html",{
        "posts": latest_posts
    })

def contact(request):
    return render(request,"blog/contact.html")

def about(request):
    return render(request,"blog/about.html")

def blog(request):
    return render(request,"blog/blog.html")

def posts(request):
    return render(request,"blog/all_posts.html",{
        "all_posts":all_posts
    })