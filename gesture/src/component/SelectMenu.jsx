import React from "react";
import { useNavigate } from "react-router-dom";
import HandsModel from "./HandsModel";

/**
 * 첫 페이지 (메뉴 선택하기)
 * author : 신지영
 * date : 2023.10.20 ~
 */

const SelectMenu = () => {
  const navigate = useNavigate();

  //볼륨조절 버튼 클릭
  const controllVolume = () => {
    navigate("/volume");
  };

  //화면조절 버튼 클릭
  const controllScreen = () => {
    navigate("/screen");
  };

  return (
    <div className="text-white text-3xl m-auto pt-40">
      <HandsModel />
      <div className="text-center ">
        <p>손가락 제스쳐를 활용해 볼륨을 조절하고</p>
        <p>화면캡쳐를 해보세요!</p>
      </div>
      <div className="my-24 grid grid-cols-4 gap-8 font-extrabold">
        <div></div>
        <button
          className="p-12 bg-gradient-to-r from-green-400 to-blue-500 hover:from-pink-500 hover:to-yellow-500 rounded-full"
          onClick={() => {
            controllVolume();
          }}
        >
          볼륨 조절
        </button>
        <button
          className="p-12 bg-gradient-to-r from-green-400 to-blue-500 hover:from-pink-500 hover:to-yellow-500 rounded-full"
          onClick={() => {
            controllScreen();
          }}
        >
          화면 캡쳐
        </button>
        <div></div>
      </div>
    </div>
  );
};

export default SelectMenu;
