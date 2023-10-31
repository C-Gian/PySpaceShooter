if fighting_boss:
    tick_to_damage_boss += 1
    if shield_as_bonus_taken:
        if laser_bool:
            for shooting_enemy in shooting_enemies_list:
                laser_as_bullet_istance_one.collide()

        # check the player-shooting enemy collision
        for shooting_enemy in shooting_enemies_list:
            shooting_enemy.collisionShootingEnemyPlayer(player_one_istance, first_player_spaceship_image)
            for bullet2 in bullets_list:
                bullet2.collisionBulletShooingEnemy(shooting_enemy, shooting_enemy_image)
        if tick_to_damage_boss > 300:
            for bullet2 in bullets_list:
                bullet2.collisionBulletBoss(boss_one_istance, asteroid_boss_image)
    else:
        if tick_immune_after_shield_boss > 0:
            tick_immune_after_shield_boss -= 1

            if laser_bool:
                for shooting_enemy in shooting_enemies_list:
                    laser_as_bullet_istance_one.collide()

            # check the player-shooting enemy collision
            for shooting_enemy in shooting_enemies_list:
                shooting_enemy.collisionShootingEnemyPlayer(player_one_istance, first_player_spaceship_image)
                for bullet2 in bullets_list:
                    bullet2.collisionBulletShooingEnemy(shooting_enemy, shooting_enemy_image)
            if tick_to_damage_boss > 300:
                for bullet2 in bullets_list:
                    bullet2.collisionBulletBoss(boss_one_istance, asteroid_boss_image)
        else:
            # check if the boss collide with the player
            boss_one_istance.collisionBoss(player_one_istance, first_player_spaceship_image)

            if laser_bool:
                for shooting_enemy in shooting_enemies_list:
                    laser_as_bullet_istance_one.collide()

            # check the player-shooting enemy collision
            for shooting_enemy in shooting_enemies_list:
                shooting_enemy.collisionShootingEnemyPlayer(player_one_istance, first_player_spaceship_image)
                for bullet2 in bullets_list:
                    bullet2.collisionBulletShooingEnemy(shooting_enemy, shooting_enemy_image)
            if tick_to_damage_boss > 300:
                for bullet2 in bullets_list:
                    bullet2.collisionBulletBoss(boss_one_istance, asteroid_boss_image)