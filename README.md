# Django Celery WebSocket and WebRTC Learning Project

This project demonstrates the use of Python 3.12, Django 5.1, Celery, WebSocket, and WebRTC. It focuses on asynchronous task management with Celery, real-time communication with WebSocket, and peer-to-peer communication with WebRTC.

## Features

- **Batch User Status Update**: Updates the status of users to "present" in batches using Celery.
- **Real-time Monitoring**: Future features will include real-time monitoring of user actions such as marking present, breaks, and exits.
- **Scheduled Updates**: Set default times to automatically update user statuses.

## Requirements

- Python 3.12
- Django 5.1
- Celery
- Redis (for Celery broker)
- WebSocket
- WebRTC

## Celery Beat

Celery Beat is a scheduler that tracks all scheduled tasks and sends them to the message broker according to the defined schedule. This allows you to perform periodic operations, such as daily updates or timed tasks. After a server restart, Celery Beat will resume tracking and scheduling tasks as specified.

**Command to execute:**

```bash
celery -A config beat --loglevel=info
```

**Note:** Celery Beat is necessary for scheduling tasks. If you don’t have scheduled tasks, you don't need to run Celery Beat.

## Celery Worker
Celery Worker is a process that executes asynchronous tasks defined in your Django project. It continuously monitors the message broker (e.g., Redis) for new tasks and processes them in the background, enabling your application to handle long-running operations efficiently.

**Command to execute:** 
```bash
celery -A config worker --loglevel=info
```