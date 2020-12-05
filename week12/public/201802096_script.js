const socket = io('/');
const videogrid = document.getElementById('video-grid');
const mypeer = new Peer();

const myvideo = document.createElement('video');
myvideo.muted = true;
const peers = {}

navigator.mediaDevices.getUserMedia({
    video: true,
    audio: true
}).then(stream => {
    addVideoStream((myvideo, stream));
    mypeer.on('call', (call) => {
        call.answer(stream);
        const video = document.createElement('video');
        call.on('stream', (userVideoStream) => {
          addVideoStream(video, userVideoStream);
        });
    });
    socket.on('user-connected', (userId) => {
        connectToNewUser(userId, stream);
    });
});

mypeer.on('open', id => {
    socket.emit('join-room', ROOM_ID, id);
});

socket.on('user-disconnected', (userId) => {
    if(peers[userId]) peers[userId].close();
});

function connectToNewUser(userId, stream) {
    const call = mypeer.call(userId, stream);
    const video = document.createElement('video');
    
    call.on('stream', userVideoStream => {
        call.addVideoStream(video, userVideoStream);
    });

    call.on('close', () => {
        video.remove();
    });

    peers[userId] = call;
    console.log(userId);
};

function addVideoStream(my_video, stream) {
    my_video.srcObject = stream;
    my_video.addEventListener('loadedmetadata', () => {
        my_video.play();
    });
    videogrid.append(my_video);
}