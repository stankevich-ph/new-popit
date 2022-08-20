// Получаем элемент кнопки и вешаем на событие "клик" вызов функции toggleDropDown
let myDropdownBtn = document.querySelector("#dropdownBtn");
myDropdownBtn.addEventListener("click", toggleDropDown);

// функция берет элемент dropdown и переключает ему класс active
function toggleDropDown() {
  let dropdownElem = document.querySelector("#myDropdown");
  dropdownElem.classList.toggle("active");
}