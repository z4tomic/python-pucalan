ESX = nil
local Users = {}

TriggerEvent('esx:getSharedObject', function(obj) ESX = obj end)

ESX.RegisterServerCallback('esx_thief:getValue', function(source, cb, targetSID) -- notifica en la consola que alguien robo (para registrar en los logs de discord)
	if Users[targetSID] then
		cb(Users[targetSID])
	else
		cb({value = false, time = 0})
	end
end)

ESX.RegisterServerCallback('esx_thief:getOtherPlayerData', function(source, cb, target)
	local xPlayer = ESX.GetPlayerFromId(target)

	local data = { -- obtener la informacion del sujeto que roban
		name = GetPlayerName(target),
		inventory = xPlayer.inventory,
		accounts = xPlayer.accounts,
		money = xPlayer.getMoney()
	}

	cb(data)
end)

RegisterServerEvent('esx_thief:stealPlayerItem')
AddEventHandler('esx_thief:stealPlayerItem', function(target, itemType, itemName, amount)
	local _source = source
	local sourceXPlayer = ESX.GetPlayerFromId(_source)
	local targetXPlayer = ESX.GetPlayerFromId(target)

	if itemType == 'item_standard' then

		local label = sourceXPlayer.getInventoryItem(itemName).label
		local itemLimit = sourceXPlayer.getInventoryItem(itemName).limit
		local sourceItemCount = sourceXPlayer.getInventoryItem(itemName).count
		local targetItemCount = targetXPlayer.getInventoryItem(itemName).count

		if amount > 0 and targetItemCount >= amount then
			if itemLimit ~= -1 and (sourceItemCount + amount) > itemLimit then
				TriggerClientEvent('esx:showNotification', targetXPlayer.source, _U('ex_inv_lim_target'))  -- obtiene la info del inventario del robado
				TriggerClientEvent('esx:showNotification', sourceXPlayer.source, _U('ex_inv_lim_source'))  -- obtiene la info del inventario del asaltante
			else
				targetXPlayer.removeInventoryItem(itemName, amount)
				sourceXPlayer.addInventoryItem(itemName, amount)

				TriggerClientEvent('esx:showNotification', sourceXPlayer.source, _U('you_stole') .. ' ~g~x' .. amount .. ' ' .. label .. ' ~w~' .. _U('from_your_target') ) -- muestra en la pantalla una notificacion de que robaste x cantidad de x cosa
				TriggerClientEvent('esx:showNotification', targetXPlayer.source, _U('someone_stole') .. ' ~r~x'  .. amount .. ' ' .. label ) -- notif de que robe x cantidad de x cosa
			end
		else
			TriggerClientEvent('esx:showNotification', _source, _U('invalid_quantity')) -- notificacion en pantalla de que la cantidad que pusiste de x cosa es invalida
		end

	elseif itemType == 'item_money' then -- estblece que el dinero es un item

		if amount > 0 and targetXPlayer.get('money') >= amount then
			targetXPlayer.removeMoney(amount) -- robar dinero
			sourceXPlayer.addMoney(amount) -- dar dinero

			TriggerClientEvent('esx:showNotification', sourceXPlayer.source, _U('you_stole') .. ' ~g~$' .. amount .. ' ~w~' .. _U('from_your_target') ) -- notif de que "tu robaste x cantidad del objetivo"
			TriggerClientEvent('esx:showNotification', targetXPlayer.source, _U('someone_stole') .. ' ~r~$'  .. amount ) -- notif al que roban que "alguien le robo x cantidad"
		else
			TriggerClientEvent('esx:showNotification', _source, _U('imp_invalid_amount')) -- notif de "cantidad invalida"
		end

	elseif itemType == 'item_account' then -- establece el dinero negro como item

		if amount > 0 and targetXPlayer.getAccount(itemName).money >= amount then
			targetXPlayer.removeAccountMoney(itemName, amount) -- quitar dinero que robaron
			sourceXPlayer.addAccountMoney(itemName, amount) -- dar el dinero que robo

			TriggerClientEvent('esx:showNotification', sourceXPlayer.source, _U('you_stole') .. ' ~g~$' .. amount .. ' ~w~' .. _U('of_black_money') .. ' ' .. _U('from_your_target') ) -- notif que robaste x cantidad de dinero sucio
			TriggerClientEvent('esx:showNotification', targetXPlayer.source, _U('someone_stole') .. ' ~r~$'  .. amount .. ' ~w~' .. _U('of_black_money') ) -- notif al que robaron, "alguien robo x cantidad de dinero negro"
		else
			TriggerClientEvent('esx:showNotification', _source, _U('imp_invalid_amount')) -- notif "cantidad invalida"
		end

	end
end)

RegisterServerEvent('esx_thief:update')
AddEventHandler('esx_thief:update', function(bool)
	local _source = source
	Users[_source] = {value = bool, time = os.time()}
end)

RegisterServerEvent('esx_thief:getValue')
AddEventHandler('esx_thief:getValue', function(targetSID)
	local _source = source
	if Users[targetSID] then
		TriggerClientEvent('esx_thief:returnValue', _source, Users[targetSID])
	else
		TriggerClientEvent('esx_thief:returnValue', _source, Users[targetSID])
	end
end)


-- sourceXPlayer = al ladron
-- targetXPlayer = al obejtivo/persona que robaron
-- RegisterServerEvent = registrar un evento del script en el servidor
-- TriggerEvent = evento que depende de lo que haga el jugador