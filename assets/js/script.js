// header
const headerNav = document.querySelector('.nav')

document.querySelector('.burger').addEventListener('click', () => {
    headerNav.classList.add('active')
})
document.querySelector('.close-nav').addEventListener('click', () => {
    headerNav.classList.remove('active')
})

// footer
const date = new Date()
document.querySelector('.copyright .container span').textContent = String(date.getFullYear())