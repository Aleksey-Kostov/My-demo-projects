// Function to update message counts
function updateMessageCounts() {
    const unreadMessages = document.querySelectorAll('.message-card.unread').length;
    const readMessages = document.querySelectorAll('.message-card.read').length;

    const totalMessages = unreadMessages + readMessages;

    document.getElementById('unreadCount').setAttribute('data-count', unreadMessages);
    document.getElementById('readCount').setAttribute('data-count', readMessages);
    document.getElementById('allCount').setAttribute('data-count', totalMessages);
}

// Function to filter messages by status
function filterMessages(status) {
    const messageCards = document.querySelectorAll('.message-card');
    messageCards.forEach(card => {
        const cardStatus = card.getAttribute('data-status');
        if (status === 'all' || cardStatus === status) {
            card.style.display = 'block';
        } else {
            card.style.display = 'none';
        }
    });
}

// Function to delete a message
function deleteMessage(button) {
    const messageItem = button.closest('.message-card');
    if (messageItem) {
        messageItem.remove();
        updateMessageCounts();
    }
}

// Update message counts when the page is loaded
document.addEventListener('DOMContentLoaded', updateMessageCounts);
