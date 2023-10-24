import React from "react";
import { useNavigate } from "react-router-dom";

const Volume = () => {
  const navigate = useNavigate();
  //메인으로 이동하기 버튼
  const goToMain = () => {
    navigate("/");
  };
  return (
    <div className="text-white text-center">
      <div className="text-4xl pt-36">손가락으로 볼륨조절하기</div>
      <div className="text-xl pt-5">
        엄지와 검지 손가락으로 볼륨을 조절할 수 있어요.
      </div>
      <div className="pt-1">
        (약지 손가락이 접혀 있을 때에만 볼륨 조절이 가능해요)
      </div>
      <img
        src="http://127.0.0.1:5000/video_frame_volume"
        className="m-auto pt-12"
      />
      <button
        className="px-10 py-5 mt-5 bg-gradient-to-r from-green-400 to-blue-500 hover:from-pink-500 hover:to-yellow-500 rounded-full"
        onClick={() => {
          goToMain();
        }}
      >
        돌아가기
      </button>
    </div>
  );
};

export default Volume;
