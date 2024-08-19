def success_logs_payload():
    return {
        "log_type": "ATTENDANCE",
        "status": "success",
        "log_data": {
            "task": "update_active_user_status_to_present",
            "error_details": "",
        },
    }

def failed_logs_payload():
    return {
        "log_type": "ATTENDANCE",
        "status": "failed",
        "log_data": {
            "task": "update_active_user_status_to_present",
            "error_details": "abcd",
        },
    }
