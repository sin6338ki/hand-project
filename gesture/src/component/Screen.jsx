import React, { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";

const Screen = () => {
  const navigate = useNavigate();
  //메인으로 이동하기 버튼
  const goToMain = () => {
    navigate("/");
  };

  return (
    <div className="text-white text-center">
      <div className="text-4xl pt-24">화면 캡쳐하기</div>
      <div className="text-xl pt-7">
        영상 화면 캡처 방법 2가지
        <div className="text-lg pt-2">
          1. 주먹을 폈다 쥐면 영상을 캡쳐할 수 있어요.
        </div>
        <div className="text-lg">2. 브이를 하면 영상을 캡쳐할 수 있어요.</div>
      </div>
      <div className="pt-1">(캡쳐된 사진은 자동으로 저장됩니다.)</div>
      <img
        src="http://127.0.0.1:5000/video_frame_screen"
        className="m-auto pt-12"
      />
      <button
        className="w-52 px-10 py-5 mt-5 mx-2 bg-gradient-to-r from-green-400 to-blue-500 hover:from-pink-500 hover:to-yellow-500 rounded-full"
        onClick={() => {
          goToMain();
        }}
      >
        돌아가기
      </button>
    </div>
  );
};

export default Screen;
