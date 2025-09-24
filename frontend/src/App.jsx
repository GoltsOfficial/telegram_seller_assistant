import { useEffect } from 'react'
import './App.css'
// Импортируем SDK Telegram WebApp
import WebApp from '@twa-dev/sdk'

function App() {
  // Инициализируем приложение при загрузке
  useEffect(() => {
    WebApp.ready();
    // Раскрываем приложение на весь экран
    WebApp.expand();
  }, []);

  // Функция для обработки нажатия на кнопку тарифа
  const handleOrder = (planName, months) => {
    // Данные, которые мы отправим боту
    const data = {
      plan: planName,
      months: months,
      user_id: WebApp.initDataUnsafe.user?.id, // ID пользователя в Telegram
    };

    // Отправляем данные в бот и закрываем приложение
    WebApp.sendData(JSON.stringify(data));
    // Закрываем мини-приложение
    WebApp.close();
  };

  // Массив с тарифами
  const tariffPlans = [
    { name: '1 месяц', months: 1, price: 'XXX руб.', id: 1 },
    { name: '3 месяца', months: 3, price: 'XXX руб.', id: 2 },
    { name: '6 месяцев', months: 6, price: 'XXX руб.', id: 3 },
    { name: '1 год', months: 12, price: 'XXX руб.', id: 4 },
  ];

  return (
    <div className="app">
      <header className="app-header">
        <h1>Заказ рекламы</h1>
        <p>Выберите срок размещения</p>
      </header>
      <main className="tariff-list">
        {tariffPlans.map((plan) => (
          <div key={plan.id} className="tariff-card">
            <h3>{plan.name}</h3>
            <p className="price">{plan.price}</p>
            <button
              onClick={() => handleOrder(plan.name, plan.months)}
              className="order-button"
            >
              Выбрать
            </button>
          </div>
        ))}
      </main>
      <footer className="app-footer">
        <p>По всем вопросам обращайтесь в поддержку.</p>
      </footer>
    </div>
  )
}

export default App