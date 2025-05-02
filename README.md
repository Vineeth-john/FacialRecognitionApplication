# Facial Recognition Applications Using Convolutional Neural Networks

## Overview

In this project, we implement a facial identification and emotion recognition model in real-time using TensorFlow, Keras, and OpenCV. The project combines Computer Vision techniques with Deep Learning to achieve accurate results.

## Components

### Facial Emotion Recognition

The emotion recognition model is implemented in `Facial_Expression_Recognition_Model.ipynb`. It utilizes Convolutional Neural Networks to classify emotions into 6 categories: Anger, Neutral, Fear, Happy, Sad, and Surprise. The trained model is saved as `model.h5`.

### Facial Identification

Facial identification is performed using `create_data.py`. This script captures 30 frames of a subject's face via webcam and stores them at a specified location on the system.

### Integration

`main_new.py` integrates both features into a single program. It accesses the webcam in real-time and performs both facial identification and emotion recognition on the subject.



# 🛒 BuyMe – Customer Representative Dashboard

This repository contains the **Customer Representative Front-End Module** of **BuyMe**, an e-commerce auction platform. This dashboard enables support reps to manage auctions, users, customer queries, and account operations with a clean UI powered by Bootstrap and vanilla JavaScript.

---

## 🚀 Features

The Customer Rep module supports the following functionalities:

- **Dashboard Overview** – Welcome landing page with sidebar navigation.
- **Profile Management**
  - View rep profile details (Rep ID, Department, Shift, etc.)
  - Update department and shift via a form.
- **User Management**
  - Search users by email.
  - Update buyer/seller usernames and emails.
  - Delete user accounts.
- **Password Reset**
  - Generate temporary passwords for users via email lookup.
- **Auction & Bid Oversight**
  - View auctions with metadata (item, brand, category, etc.)
  - View auction details and item specifications in modals.
  - Delete auctions or individual bids.
- **Customer Queries**
  - View unresolved queries submitted by users.
  - Respond directly via text input.
  - Mark queries as resolved.

---

## 📁 File Structure



