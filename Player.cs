using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class Player : MonoBehaviour {

	[Tooltip("Префаб снаряда")]
	public GameObject fireballPrefab;

	[Tooltip("Точка вылета снаряда")]
	public Transform attackPoint;

	[Tooltip("Количество монеток, которые собрал Игрок")]
	public int coins = 0;

	[Tooltip("Максимальное здоровье Игрока")]
	public int healthMax = 10;
	[Tooltip("Текущее здоровье Игрока")]
	public int health = 10;

	[Tooltip("Компонент, отвечающий за анимацию полчучения урона")]
	public Animator damageMaskAnimator;

	[Tooltip("Компонент, отвечающий за проигрывание звуков Игрока")]
	public AudioSource audioSource;
	[Tooltip("Звуковой файл звука получения урона")]
	public AudioClip damageSound;

	void Update () {

		// Если игрок кликает левой кнопкой мыши
		// создать огненный шар
		if (Input.GetMouseButtonDown (0)) {
			Instantiate (fireballPrefab, attackPoint.position, attackPoint.rotation);
		}

	}

	// Обработка входного урона
	public void TakeDamage()
	{
		health--;

		// Если здоровье все еще больше 0
		if (health > 0) 
		{
			// Проигрываем анимацию получения урона
			damageMaskAnimator.SetTrigger("play");
			// Проигрываем звук получения урона
			audioSource.PlayOneShot (damageSound);
		}
		// Если здоровье меньше или равно 0
		else 
		{
			// Перезагружаем текущую сцену
			int sceneIndex = SceneManager.GetActiveScene ().buildIndex;
			SceneManager.LoadScene (sceneIndex);
		}
	}
}
