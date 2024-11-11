// Function to update message counts
function updateMessageCounts() {
    const unreadMessages = document.querySelectorAll('.message-item.unread').length;
    const readMessages = document.querySelectorAll('.message-item.read').length;
    
    const totalMessages = unreadMessages + readMessages;

    document.getElementById('unreadCount').setAttribute('data-count', unreadMessages);
    document.getElementById('readCount').setAttribute('data-count', readMessages);
    document.getElementById('allCount').setAttribute('data-count', totalMessages);
}

function filterMessages(filterType) {
    const allMessages = document.querySelectorAll('.message-item');
    
    allMessages.forEach(message => {
        if (filterType === 'all') {
            message.classList.remove('hidden');
        } else if (filterType === 'unread' && message.classList.contains('unread')) {
            message.classList.remove('hidden');
        } else if (filterType === 'read' && message.classList.contains('read')) {
            message.classList.remove('hidden');
        } else {
            message.classList.add('hidden');
        }
    });
}

function deleteMessage(button) {
    const messageItem = button.closest('.message-item');
    if (messageItem) {
        messageItem.remove();
        updateMessageCounts();
    }
}

document.addEventListener('DOMContentLoaded', updateMessageCounts);
